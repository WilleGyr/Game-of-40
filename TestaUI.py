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

    # Går till huvudmenyn
    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Går till huvudmenyn som gästa
    def Goto_MainMenuGuest(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)
        global CurrentUser

        # Skapar ett temporärt namn till en gästanvändare
        CurrentUser = "Guest"
        for x in range(10):
            RandomInt = randrange(10)
            CurrentUser += str(RandomInt)
            
        w=open("CurrentUser.txt", "w")
        w.writable()
        w.write(CurrentUser)
        w.close()
        print("CurrentUser: {}".format(CurrentUser))

    # Går till Signup-menyn
    def Goto_SignupWindow(self):
        signupwindow=SignupWindow()
        widget.addWidget(signupwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Går till inloggningsmenyn
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

    # Går till huvudmenyn
    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Loggar in
    def LoginNextClicked(self):
        Logins = open("Logins.txt").read().splitlines()
        global LoginUsername, LoginPassword
        LoginUsername = self.LoginUsername.text()
        LoginPassword = self.LoginPassword.text()
        Combo = LoginUsername + ":" + LoginPassword
        print (Combo)

        # Kollar om användarnamnet och lösenordet är kopplade till ett konto
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
    
    # Går till startmenyn
    def Goto_StartWindow(self):
        startwindow=StartWindow()
        widget.addWidget(startwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Skapar ett konto
    def SignupNextClicked(self):
        UsernameValid = True
        Logins = open("Logins.txt").read().splitlines()
        SignupUsername = str(self.SignupUsername.text())
        
        # Lagrar användarnamnet och lösenordet i ett textdokument om användarnamnet inte används redan
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

    # Visar inställningarna för spelläget där man möter en annan spelare
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
    
    # Visar inställningarna för spelläget där man möter datorn
    def ComputerClicked(self):
        global DiffLvl, OppName
        self.PlayBtn.show()
        self.PlayLabel.hide()
        self.OppName.hide()
        self.NamnOpp.hide()
        self.DiffDrop.show()
        self.DiffLabel.show()
        OppName = "Computer"
        self.PlayBtn.clicked.connect(self.Goto_GameWindowAI)

    # Går till spelmenyn mot dator
    def Goto_GameWindowAI(self):
        OppName = "Computer"
        w=open("OpponentName.txt", "w")
        w.writable()
        w.write(OppName)
        w.close()

        Difflvl = self.DiffDrop.currentText()
        w=open("Diff.txt", "w")
        w.writable()
        w.write(str(Difflvl))
        w.close()

        gamewindowai=GameWindowAI()
        widget.addWidget(gamewindowai)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    # Går till spelmenyn mot annan spelare
    def Goto_GameWindowVers(self):
        OppName = self.NamnOpp.text()

        w=open("OpponentName.txt", "w")
        w.writable()
        w.write(OppName)
        w.close()

        gamewindow=GameWindow()
        widget.addWidget(gamewindow)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
    # Går till spelmenyn
    def Goto_GameWindow_Vs(self):
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
        
    def Goto_GameWindow_AI(self):
        global CurrentUser
        DiffLvl = self.DiffDrop.currentText()
        OppName = self.NamnOpp.text()
        w=open("CurrentUser.txt", "r")
        CurrentUser = w.read()
        w.close()
        print(DiffLvl+" --- "+OppName)

        gamewindowai=GameWindowAI()
        widget.addWidget(gamewindowai)
        widget.setCurrentIndex(widget.currentIndex()+1)
        
class GameWindowAI(QMainWindow):
    def __init__(self):
        super(GameWindowAI, self).__init__()
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
        global Difflvl
        w=open("Diff.txt", "r")
        Difflvl=w.read()

        global game_active
        game_active = True
        self.turn_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.current_roll = 0
        self.LineMe.show()
        self.LineOpp.hide()
        self.RollBtn.clicked.connect(self.roll)
        self.SaveBtn.clicked.connect(self.endTurn)

    def roll(self):
        
        

        # Slår tärningen
        if game_active == True:
            self.current_roll = randint(1, 6)

            if self.current_roll == 6:
                self.turn_score = 0
                self.endTurn()
            else:
                self.turn_score += self.current_roll
            

            # Uppdaterar scoreboarden
            self.CurrentScore.setText(str(self.current_roll))
            self.ScoreMe.setText(str(self.player1_score))
            self.ScoreOpp.setText(str(self.player2_score))
            
            self.checkForWinner()
        
    def roll_ai(self):
        if Difflvl == "Easy":
            range1=2
            for x in range(range1):
                self.currentrollai = randint(1,6)
                if self.currentrollai == 6:
                    range1=0
                    self.endTurn()
                else:
                    self.turn_score += self.current_roll


        if Difflvl == "Normal":
            playing = True
            while playing is True:
                det_playing = random.choice([0,1])
                if det_playing == 0:
                    playing = False
                else:
                    playing = True
                self.currentrollai = randint(1,6)
                if self.currentrollai == 6:
                    playing = False
                    self.endTurn()
                else:
                    self.turn_score += self.currentrollai

        if Difflvl == "Hard":
            self.currentrollai = randint(1,6)

        elif Difflvl == "Impossible":
            self.currentrollai = randint(1,5)

    def endTurn(self):
        # Sparar poäng genom att addera rondens poäng till spelarens totala poäng
        if game_active == True:
            if self.current_player == 1:
                self.player1_score += self.turn_score
            else:
                self.player2_score += self.turn_score
            
            # Byter spelare och nollställer den aktiva rondens poäng
            if self.current_player == 1:
                self.current_player = 2
                self.LineMe.hide()
                self.LineOpp.show()
            else:
                self.current_player = 1
                self.LineMe.show()
                self.LineOpp.hide()
            self.turn_score = 0
            
            # Uppdaterar scoreboarden
            self.ScoreMe.setText(str(self.player1_score))
            self.ScoreOpp.setText(str(self.player2_score))
            self.CurrentScore.setText("0")
            
            self.checkForWinner()

    def checkForWinner(self):
        # Kollar ifall det finns en vinnare och stannar spelet isåfall
        global Winner
        if self.player1_score >= 10:
            game_active = False
            w=open("CurrentUser.txt", "r")
            CurrentUser = w.read()
            w.close()
            Winner = CurrentUser
            self.game_hide()
            self.Goto_GameEndWindow()

        elif self.player2_score >= 10:
            game_active = False
            w=open("OpponentName.txt", "r")
            OppName = w.read()
            w.close()
            Winner = OppName
            self.game_hide()
            self.Goto_GameEndWindow()

        else:
            game_active = True

    def Save(self):
        with open("PlayerScore.txt", "r") as R:
            OldScore=R.read()
        OldScore+=sum(CurrentRound)

        with open("PlayerScore.txt", "w") as W:
            W.write(OldScore)

    # Går till slutmenyn när någon har vunnit
    def Goto_GameEndWindow(self):
        gameendwindow=GameEndWindow()
        widget.addWidget(gameendwindow)
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
        
        global game_active
        game_active = True
        self.turn_score = 0
        self.player1_score = 0
        self.player2_score = 0
        self.current_player = 1
        self.current_roll = 0
        self.LineMe.show()
        self.LineOpp.hide()
        self.RollBtn.clicked.connect(self.roll)
        self.SaveBtn.clicked.connect(self.endTurn)

    def Play(self):
        global CurrentRound, OldScore



        """with open("PlayerScore.txt", "r") as R:
            OldScore=R.read()
        CurrentRound=[]
        CurrentVal=randint(1,6)
        if CurrentVal == 6:
            print("Next turn")
        else:
            self.CurrentRound.append(CurrentVal)
        if OldScore+sum(CurrentRound) >= 40:
            print("Win")"""

    def roll(self):
        
        

        # Slår tärningen
        if game_active == True:
            self.current_roll = randint(1, 6)

            if self.current_roll == 6:
                self.turn_score = 0
                self.endTurn()
            else:
                self.turn_score += self.current_roll
            

            # Uppdaterar scoreboarden
            self.CurrentScore.setText(str(self.current_roll))
            self.ScoreMe.setText(str(self.player1_score))
            self.ScoreOpp.setText(str(self.player2_score))
            
            self.checkForWinner()
        

    def endTurn(self):
        # Sparar poäng genom att addera rondens poäng till spelarens totala poäng
        if game_active == True:
            if self.current_player == 1:
                self.player1_score += self.turn_score
            else:
                self.player2_score += self.turn_score
            
            # Byter spelare och nollställer den aktiva rondens poäng
            if self.current_player == 1:
                self.current_player = 2
                self.LineMe.hide()
                self.LineOpp.show()
            else:
                self.current_player = 1
                self.LineMe.show()
                self.LineOpp.hide()
            self.turn_score = 0
            
            # Uppdaterar scoreboarden
            self.ScoreMe.setText(str(self.player1_score))
            self.ScoreOpp.setText(str(self.player2_score))
            self.CurrentScore.setText("0")
            
            self.checkForWinner()

    def checkForWinner(self):
        # Kollar ifall det finns en vinnare och stannar spelet isåfall
        global Winner
        if self.player1_score >= 10:
            game_active = False
            w=open("CurrentUser.txt", "r")
            CurrentUser = w.read()
            w.close()
            Winner = CurrentUser
            self.game_hide()
            self.Goto_GameEndWindow()

        elif self.player2_score >= 10:
            game_active = False
            w=open("OpponentName.txt", "r")
            OppName = w.read()
            w.close()
            Winner = OppName
            self.game_hide()
            self.Goto_GameEndWindow()

        else:
            game_active = True

    def Save(self):
        with open("PlayerScore.txt", "r") as R:
            OldScore=R.read()
        OldScore+=sum(CurrentRound)

        with open("PlayerScore.txt", "w") as W:
            W.write(OldScore)

    # Går till slutmenyn när någon har vunnit
    def Goto_GameEndWindow(self):
        gameendwindow=GameEndWindow()
        widget.addWidget(gameendwindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

class GameEndWindow(QMainWindow):
    def __init__(self):
        super(GameEndWindow, self).__init__()
        loadUi("GameEndWindow.ui", self)

        w=open("CurrentUser.txt", "r")
        CurrentUser = w.read()
        w.close()
        w=open("OpponentName.txt", "r")
        OppName = w.read()
        w.close()

        self.WonLossLabel.setText(Winner+" WINS!!!")
        self.PlayAgain.clicked.connect(self.Goto_GameWindow)
        self.EndMainMenu.clicked.connect(self.Goto_MainMenu)

    # Går tillbaka till spelmenyn
    def Goto_GameWindow(self):
        global CurrentUser
        w=open("CurrentUser.txt", "r")
        CurrentUser = w.read()
        w.close()

        gamewindow=GameWindow()
        widget.addWidget(gamewindow)
        widget.setCurrentIndex(widget.currentIndex()+1)

    # Går tillbaka till huvudmenyn
    def Goto_MainMenu(self):
        mainmenu=MainMenu()
        widget.addWidget(mainmenu)
        widget.setCurrentIndex(widget.currentIndex()+1)

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