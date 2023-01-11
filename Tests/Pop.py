from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Popup(object):
    def setupUi(self, Popup):
        Popup.setObjectName("Popup")
        Popup.resize(150, 200)
        Popup.setFixedSize(150, 200)
        self.buttonBox = QtWidgets.QDialogButtonBox(Popup)
        self.buttonBox.setGeometry(QtCore.QRect(10, 440, 621, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Popup)
        self.label.setGeometry(QtCore.QRect(50, 20, 241, 131))
        font = QtGui.QFont()
        font.setPointSize(25)
        self.label.setFont(font)
        self.label.setObjectName("label")
        #self.setFixedSize(300, 300)

        self.retranslateUi(Popup)
        self.buttonBox.accepted.connect(Popup.accept) # type: ignore
        self.buttonBox.rejected.connect(Popup.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Popup)

    def retranslateUi(self, Popup):
        _translate = QtCore.QCoreApplication.translate
        Popup.setWindowTitle(_translate("Popup", "Dialog"))
        self.label.setText(_translate("Popup", "Hellluuuuuuu"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Popup = QtWidgets.QDialog()
    ui = Ui_Popup()
    ui.setupUi(Popup)
    Popup.show()
    sys.exit(app.exec_())
