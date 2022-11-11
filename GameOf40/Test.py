from PyQt5 import QtCore, QtGui, QtWidgets
from Pop import Ui_Popup

class Ui_Hub(object):
    def Popup(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_Popup()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, Hub):
        Hub.setObjectName("Hub")
        Hub.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(Hub)
        self.centralwidget.setObjectName("centralwidget")
        self.Knapp = QtWidgets.QPushButton(self.centralwidget)
        self.Knapp.setGeometry(QtCore.QRect(150, 120, 311, 151))
        self.Knapp.setObjectName("Knapp")
        Hub.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(Hub)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 21))
        self.menubar.setObjectName("menubar")
        Hub.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(Hub)
        self.statusbar.setObjectName("statusbar")
        Hub.setStatusBar(self.statusbar)
        self.Knapp.clicked.connect(self.Popup)

        self.retranslateUi(Hub)
        QtCore.QMetaObject.connectSlotsByName(Hub)

    def retranslateUi(self, Hub):
        _translate = QtCore.QCoreApplication.translate
        Hub.setWindowTitle(_translate("Hub", "MainWindow"))
        self.Knapp.setText(_translate("Hub", "Hej"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Hub = QtWidgets.QMainWindow()
    ui = Ui_Hub()
    ui.setupUi(Hub)
    Hub.show()
    sys.exit(app.exec_())
