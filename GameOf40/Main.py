from PyQt5.uic import loadUi
from PyQt5 import QtWidgets, QtGui
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QPushButton, QMessageBox, QLineEdit, QHBoxLayout, QVBoxLayout, QFrame, QDialog, QMainWindow
import sys
from Test import Ui_Hub

class MainWindow(QMainWindow):
    def OpenMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Hub()
        self.ui.setupUi(self.window)
        self.window.show()
        
        self.Knapp.clicked.connect(self.launchPopup)

    #def launchPopup(self):
        #self.window



    


app = QApplication(sys.argv)
widget=QtWidgets.QStackedWidget()
mainwindow=MainWindow()
widget.addWidget(mainwindow)
widget.setFixedHeight(600)
widget.setFixedWidth(800)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")