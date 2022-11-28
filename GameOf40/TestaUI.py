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
        self.GuestBtn.clicked.connect(self.Goto_MainMenuGuest)
        self.SignupBtn.clicked.connect(self.Goto_SignupWindow)
        self.LoginBtn.clicked.connect(self.Goto_LoginWindow)

    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    def Goto_MainMenuGuest(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        global CurrentUser
        CurrentUser = "Guest"

        for x in range(10):
            RandomInt = randrange(10)
            CurrentUser += str(RandomInt)
        w=open("CurrentUser.txt", "w")
        w.writable()
        w.write(CurrentUser)
        w.close()
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
            CurrentUser = LoginUsername
            w=open("CurrentUser.txt", "w")
            w.writable()
            w.write(CurrentUser)
            w.close()
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

class MainMenu(QMainWindow):
    def __init__(self):
        super(MainMenu, self).__init__()
        loadUi("MainMenu.ui",self)
        self.PlayBtn.hide()
        self.OppName.hide()
        #self.DiffDrop.hide()
        self.NamnOpp.hide()
        #self.DiffLabel.hide()
        self.ComputerBtn.clicked.connect(self.ComputerClicked)
        self.VersusBtn.clicked.connect(self.VersusClicked)

    def VersusClicked(self):
        global OppName
        self.PlayBtn.show()
        self.PlayLabel.hide()
        self.OppName.show()
        self.NamnOpp.show()
        self.DiffDrop.hide()
        self.DiffLabel.hide()
        OppName = self.NamnOpp.text()
        self.PlayBtn.clicked.connect(self.Goto_GameWindowVers)
    
    def ComputerClicked(self):
        global DiffLvl, OppName
        self.PlayBtn.show()
        self.PlayLabel.hide()
        self.OppName.hide()
        self.NamnOpp.hide()
        self.DiffDrop.show()
        self.DiffLabel.show()
        OppName = "Computer"
        self.PlayBtn.clicked.connect(self.Goto_GameWindowComp)

    def Goto_GameWindowComp(self):
        OppName = "Computer"
        w=open("OpponentName.txt", "w")
        w.writable()
        w.write(OppName)
        w.close()
        gamewindow=GameWindow()
        widget.addWidget(gamewindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def Goto_GameWindowVers(self):
        OppName = self.NamnOpp.text()
        w=open("OpponentName.txt", "w")
        w.writable()
        w.write(OppName)
        w.close()
        gamewindow=GameWindow()
        widget.addWidget(gamewindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

    def Goto_GameWindow(self):
        global CurrentUser
        DiffLvl = self.DiffDrop.currentText()
        OppName = self.NamnOpp.text()
        w=open("CurrentUser.txt", "r")
        CurrentUser = w.read()
        w.close()
        print(DiffLvl+" --- "+OppName)
        gamewindow=GameWindow()
        widget.addWidget(gamewindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        

class GameWindow(QMainWindow):
    def __init__(self):
        super(GameWindow, self).__init__()
        loadUi("GameWindow.ui",self)
        w=open("CurrentUser.txt", "r")
        CurrentUser = w.read()
        w.close()
        w=open("OpponentName.txt", "r")
        OppName = w.read()
        w.close()
        self.ScoreNameMe.setText(CurrentUser)
        self.ScoreNameOpp.setText(OppName)
        print(OppName+":::"+CurrentUser)

    def Play(self):
        global CurrentRound, OldScore
        with open("PlayerScore.txt", "r") as R:
            OldScore=R.read()
        CurrentRound=[]
        CurrentVal=randint(1,6)
        if CurrentVal == 6:
            print("Next turn")
        else:
            self.CurrentRound.append(CurrentVal)
        if OldScore+sum(CurrentRound) >= 40:
            print("Win")

    def Save(self):
        with open("PlayerScore.txt", "r") as R:
            OldScore=R.read()
        OldScore+=sum(CurrentRound)
        with open("PlayerScore.txt", "w") as W:
            W.write(OldScore)


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