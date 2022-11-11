from calendar import week
import sys
from random import *
from this import d
from datetime import *
from PyQt5.uic import loadUi
from pytube import YouTube
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QDialog, QMainWindow

class StartWindow(QMainWindow):
    def __init__(self):
        super(StartWindow, self).__init__()
        loadUi("StartMenu.ui",self)
        self.GuestBtn.clicked.connect(self.Goto_MainMenu)
        self.SignupBtn.clicked.connect(self.Goto_SignupWindow)
        self.LoginBtn.clicked.connect(self.Goto_LoginWindow)

    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        global CurrentUser
        CurrentUser = "Guest"
        for x in range(10):
            RandomInt = randrange(10)
            CurrentUser += str(RandomInt)
        print("CurrentUser: {}".format(CurrentUser))

    def Goto_SignupWindow(self):
        signupwindow=SignupWindow()
        widget.addWidget(signupwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Goto_LoginWindow(self):
        loginwindow=LoginWindow()
        widget.addWidget(loginwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class LoginWindow(QMainWindow):
    def __init__(self):
        super(LoginWindow, self).__init__()
        loadUi("LoginWindow.ui", self)
        self.WrongLogin.hide()
        self.LoginNext.clicked.connect(self.LoginNextClicked)

    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def LoginNextClicked(self):
        Logins = open("Logins.txt").read().splitlines()
        global LoginUsername, LoginPassword
        LoginUsername = self.LoginUsername.text()
        LoginPassword = self.LoginPassword.text()
        Combo = LoginUsername + ":" + LoginPassword
        print (Combo)
        if Combo in Logins:
            self.Goto_MainMenu()
        else:
            self.WrongLogin.show()


class SignupWindow(QMainWindow):
    def __init__(self):
        super(SignupWindow, self).__init__()
        loadUi("SignupWindow.ui", self)
        self.WrongSignup.hide()
        global SignupUsername, SignupPassword
        SignupUsername = str(self.SignupUsername.text())
        SignupPassword = str(self.SignupPassword.text())
        self.SignupNext.clicked.connect(self.SignupNextClicked)
        
    def Goto_StartWindow(self):
        startwindow=StartWindow()
        widget.addWidget(startwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def SignupNextClicked(self):
        UsernameValid = True
        Logins = open("Logins.txt").read().splitlines()
        SignupUsername = str(self.SignupUsername.text())
        
        for Combo in Logins:
            if SignupUsername in Combo:
                UsernameValid = False
                self.WrongSignup.show()
        if UsernameValid == True:
            SignupUsername = str(self.SignupUsername.text())
            SignupPassword = str(self.SignupPassword.text())
            Combo = SignupUsername + ":" + SignupPassword

            f1 = open("Logins.txt", "a+")
            f1.writable()
            f1.write(Combo + "\n")
            f1.close()
            self.Goto_StartWindow()
        #print (SignupUsername, SignupPassword)

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("MainMenu.ui",self)

app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=StartWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(900)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")