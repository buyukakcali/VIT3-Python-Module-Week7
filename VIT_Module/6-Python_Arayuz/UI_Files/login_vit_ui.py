# Form implementation generated from reading ui file 'UI_Files/login_vit_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(350, 350)
        MainWindow.setMinimumSize(QtCore.QSize(350, 350))
        MainWindow.setMaximumSize(QtCore.QSize(350, 350))
        MainWindow.setFocusPolicy(QtCore.Qt.FocusPolicy.ClickFocus)
        MainWindow.setWindowTitle("LOGIN")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/logo_organization1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.499773, y1:1, x2:0.5, y2:0.00568182, stop:0 rgba(0, 0, 0, 255), stop:1 rgba(255, 255, 255, 255));\n"
"One value - border-radius: 100px;")
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButtonLogin = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonLogin.setGeometry(QtCore.QRect(80, 200, 91, 31))
        self.pushButtonLogin.setMouseTracking(True)
        self.pushButtonLogin.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButtonLogin.setStyleSheet("\n"
"QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
" \n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"    \n"
"}\n"
"\n"
"")
        self.pushButtonLogin.setObjectName("pushButtonLogin")
        self.pushButtonExit = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonExit.setGeometry(QtCore.QRect(250, 275, 91, 31))
        self.pushButtonExit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}\n"
"")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.lineEditUsername = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditUsername.setGeometry(QtCore.QRect(80, 100, 191, 31))
        self.lineEditUsername.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEditUsername.setStyleSheet("QLineEdit {\n"
"  border: 2px solid rgb(38, 38, 48);\n"
"  border-radius: 15px;\n"
"  color: #FFF;\n"
"  padding-left: 15px;\n"
"  background-color: rgba(0, 0, 0,55%);\n"
" \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"\n"
" QLineEdit:focus  {\n"
"  border: 2px solid rgb(35, 218, 233);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"\n"
"   \n"
"\n"
"\n"
"\n"
"")
        self.lineEditUsername.setText("")
        self.lineEditUsername.setCursorPosition(0)
        self.lineEditUsername.setObjectName("lineEditUsername")
        self.lineEditPassword = QtWidgets.QLineEdit(parent=self.centralwidget)
        self.lineEditPassword.setGeometry(QtCore.QRect(80, 140, 191, 31))
        self.lineEditPassword.setStyleSheet("QLineEdit {\n"
"  border: 2px solid rgb(38, 38, 48);\n"
"  border-radius: 15px;\n"
"  color: #FFF;\n"
"  padding-left: 15px;\n"
"  background-color: rgba(0, 0, 0,55%);\n"
" \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(0, 255, 255);\n"
"}\n"
"\n"
" QLineEdit:focus  {\n"
"  border: 2px solid rgb(35, 218, 233);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"")
        self.lineEditPassword.setText("")
        self.lineEditPassword.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.lineEditPassword.setObjectName("lineEditPassword")
        self.labelLogo2 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelLogo2.setGeometry(QtCore.QRect(105, 35, 185, 40))
        self.labelLogo2.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.labelLogo2.setText("")
        self.labelLogo2.setPixmap(QtGui.QPixmap("UI_Files\\pictures/logo_organization2.png"))
        self.labelLogo2.setScaledContents(True)
        self.labelLogo2.setObjectName("labelLogo2")
        self.pushButtonForgot = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonForgot.setGeometry(QtCore.QRect(90, 250, 181, 21))
        self.pushButtonForgot.setStyleSheet("QPushButton{\n"
"    border-radius : 10px;\n"
"    background-color: rgba(0, 0, 0,0%);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(107, 107, 107);\n"
"}")
        self.pushButtonForgot.setObjectName("pushButtonForgot")
        self.labelFail = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelFail.setGeometry(QtCore.QRect(80, 175, 201, 21))
        self.labelFail.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(189, 31, 57);\n"
"border-radius : 15px;")
        self.labelFail.setScaledContents(False)
        self.labelFail.setObjectName("labelFail")
        self.checkBoxPassword = QtWidgets.QCheckBox(parent=self.centralwidget)
        self.checkBoxPassword.setGeometry(QtCore.QRect(280, 140, 51, 31))
        self.checkBoxPassword.setStyleSheet("background-color: rgba(0, 0, 0, 0);\n"
"color: rgb(255, 255, 255);")
        self.checkBoxPassword.setObjectName("checkBoxPassword")
        self.pushButtonBack = QtWidgets.QPushButton(parent=self.centralwidget)
        self.pushButtonBack.setGeometry(QtCore.QRect(190, 200, 91, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(False)
        self.pushButtonBack.setFont(font)
        self.pushButtonBack.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(162, 0, 0);\n"
"}\n"
"")
        self.pushButtonBack.setIconSize(QtCore.QSize(60, 60))
        self.pushButtonBack.setObjectName("pushButtonBack")
        self.labelLogo1 = QtWidgets.QLabel(parent=self.centralwidget)
        self.labelLogo1.setGeometry(QtCore.QRect(40, 20, 65, 70))
        self.labelLogo1.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.labelLogo1.setText("")
        self.labelLogo1.setPixmap(QtGui.QPixmap("UI_Files\\pictures/logo_organization1.ico"))
        self.labelLogo1.setScaledContents(True)
        self.labelLogo1.setObjectName("labelLogo1")
        self.pushButtonExit.raise_()
        self.lineEditUsername.raise_()
        self.lineEditPassword.raise_()
        self.labelLogo2.raise_()
        self.pushButtonForgot.raise_()
        self.labelFail.raise_()
        self.pushButtonLogin.raise_()
        self.checkBoxPassword.raise_()
        self.pushButtonBack.raise_()
        self.labelLogo1.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(parent=MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 350, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.lineEditUsername, self.lineEditPassword)
        MainWindow.setTabOrder(self.lineEditPassword, self.pushButtonLogin)
        MainWindow.setTabOrder(self.pushButtonLogin, self.pushButtonExit)
        MainWindow.setTabOrder(self.pushButtonExit, self.pushButtonForgot)
        MainWindow.setTabOrder(self.pushButtonForgot, self.checkBoxPassword)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        self.pushButtonLogin.setText(_translate("MainWindow", "Login"))
        self.pushButtonExit.setText(_translate("MainWindow", "Exit"))
        self.lineEditUsername.setPlaceholderText(_translate("MainWindow", "username"))
        self.lineEditPassword.setPlaceholderText(_translate("MainWindow", "password"))
        self.pushButtonForgot.setText(_translate("MainWindow", "Forgot password.?"))
        self.labelFail.setText(_translate("MainWindow", "<html><head/><body><p><br/></p></body></html>"))
        self.checkBoxPassword.setText(_translate("MainWindow", "Show"))
        self.pushButtonBack.setText(_translate("MainWindow", "Back"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec())
