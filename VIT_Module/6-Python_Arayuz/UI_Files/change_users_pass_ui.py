# Form implementation generated from reading ui file 'UI_Files/change_users_pass_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogResetUsersPasswords(object):
    def setupUi(self, DialogResetUsersPasswords):
        DialogResetUsersPasswords.setObjectName("DialogResetUsersPasswords")
        DialogResetUsersPasswords.resize(604, 410)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/logo1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DialogResetUsersPasswords.setWindowIcon(icon)
        DialogResetUsersPasswords.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));\n"
"\n"
"QToolTip { background-color: yellow; color: black; border: 1px solid black;}")
        self.frameResetUsersPasswords = QtWidgets.QFrame(parent=DialogResetUsersPasswords)
        self.frameResetUsersPasswords.setGeometry(QtCore.QRect(250, 0, 351, 411))
        self.frameResetUsersPasswords.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameResetUsersPasswords.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameResetUsersPasswords.setObjectName("frameResetUsersPasswords")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.frameResetUsersPasswords)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.labelLogo = QtWidgets.QLabel(parent=self.frameResetUsersPasswords)
        self.labelLogo.setMinimumSize(QtCore.QSize(331, 70))
        self.labelLogo.setMaximumSize(QtCore.QSize(331, 70))
        self.labelLogo.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelLogo.setFrameShape(QtWidgets.QFrame.Shape.NoFrame)
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("UI_Files\\pictures/logo2.png"))
        self.labelLogo.setScaledContents(True)
        self.labelLogo.setObjectName("labelLogo")
        self.verticalLayout_3.addWidget(self.labelLogo)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem)
        self.labelCaseName = QtWidgets.QLabel(parent=self.frameResetUsersPasswords)
        self.labelCaseName.setMinimumSize(QtCore.QSize(330, 0))
        self.labelCaseName.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setPointSize(14)
        font.setBold(True)
        font.setUnderline(True)
        self.labelCaseName.setFont(font)
        self.labelCaseName.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelCaseName.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelCaseName.setObjectName("labelCaseName")
        self.verticalLayout_3.addWidget(self.labelCaseName)
        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Policy.Minimum, QtWidgets.QSizePolicy.Policy.Expanding)
        self.verticalLayout_3.addItem(spacerItem1)
        self.line = QtWidgets.QFrame(parent=self.frameResetUsersPasswords)
        self.line.setMaximumSize(QtCore.QSize(330, 16777215))
        font = QtGui.QFont()
        font.setBold(False)
        self.line.setFont(font)
        self.line.setFrameShape(QtWidgets.QFrame.Shape.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Shadow.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_3.addWidget(self.line)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tableWidget = QtWidgets.QTableWidget(parent=self.frameResetUsersPasswords)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout_3.addLayout(self.verticalLayout_2)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButtonRUPExit = QtWidgets.QPushButton(parent=self.frameResetUsersPasswords)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonRUPExit.sizePolicy().hasHeightForWidth())
        self.pushButtonRUPExit.setSizePolicy(sizePolicy)
        self.pushButtonRUPExit.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButtonRUPExit.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonRUPExit.setMouseTracking(True)
        self.pushButtonRUPExit.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButtonRUPExit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255); \n"
"}\n"
"\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}\n"
"\n"
"QPushButton:focus  {\n"
"  border: 2px solid rgb(162, 0, 0);\n"
"}")
        self.pushButtonRUPExit.setObjectName("pushButtonRUPExit")
        self.horizontalLayout.addWidget(self.pushButtonRUPExit)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.labelUserImage = QtWidgets.QLabel(parent=DialogResetUsersPasswords)
        self.labelUserImage.setGeometry(QtCore.QRect(20, 10, 210, 210))
        self.labelUserImage.setStyleSheet("QLabel { background-color: rgb(0, 0, 0, 0); }")
        self.labelUserImage.setText("")
        self.labelUserImage.setPixmap(QtGui.QPixmap("UI_Files\\pictures/user_pic.png"))
        self.labelUserImage.setScaledContents(True)
        self.labelUserImage.setObjectName("labelUserImage")
        self.labelRightLock = QtWidgets.QLabel(parent=DialogResetUsersPasswords)
        self.labelRightLock.setGeometry(QtCore.QRect(50, 229, 131, 121))
        self.labelRightLock.setMinimumSize(QtCore.QSize(100, 100))
        self.labelRightLock.setMaximumSize(QtCore.QSize(200, 200))
        self.labelRightLock.setStyleSheet("QLabel { background-color: rgb(0, 0, 0, 0); }")
        self.labelRightLock.setText("")
        self.labelRightLock.setPixmap(QtGui.QPixmap("UI_Files\\pictures/icon_change_user_password_orj.png"))
        self.labelRightLock.setScaledContents(True)
        self.labelRightLock.setObjectName("labelRightLock")
        self.frameYellowSide = QtWidgets.QFrame(parent=DialogResetUsersPasswords)
        self.frameYellowSide.setGeometry(QtCore.QRect(-20, -10, 251, 421))
        self.frameYellowSide.setStyleSheet("")
        self.frameYellowSide.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.frameYellowSide.setFrameShadow(QtWidgets.QFrame.Shadow.Raised)
        self.frameYellowSide.setObjectName("frameYellowSide")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frameYellowSide)
        self.verticalLayout.setObjectName("verticalLayout")
        self.labelBackgroundYellow = QtWidgets.QLabel(parent=self.frameYellowSide)
        self.labelBackgroundYellow.setMinimumSize(QtCore.QSize(251, 411))
        self.labelBackgroundYellow.setStyleSheet("QFrame {\n"
"    background-color: rgb(254, 213, 1);\n"
"}")
        self.labelBackgroundYellow.setText("")
        self.labelBackgroundYellow.setPixmap(QtGui.QPixmap("UI_Files\\pictures/yellow_side_of_form.png"))
        self.labelBackgroundYellow.setObjectName("labelBackgroundYellow")
        self.verticalLayout.addWidget(self.labelBackgroundYellow)
        self.frameResetUsersPasswords.raise_()
        self.frameYellowSide.raise_()
        self.labelRightLock.raise_()
        self.labelUserImage.raise_()

        self.retranslateUi(DialogResetUsersPasswords)
        QtCore.QMetaObject.connectSlotsByName(DialogResetUsersPasswords)

    def retranslateUi(self, DialogResetUsersPasswords):
        _translate = QtCore.QCoreApplication.translate
        DialogResetUsersPasswords.setWindowTitle(_translate("DialogResetUsersPasswords", "Reset Users Passwords"))
        self.labelCaseName.setText(_translate("DialogResetUsersPasswords", "Reset Users Passwords Menu"))
        self.pushButtonRUPExit.setText(_translate("DialogResetUsersPasswords", "EXIT"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogResetUsersPasswords = QtWidgets.QDialog()
    ui = Ui_DialogResetUsersPasswords()
    ui.setupUi(DialogResetUsersPasswords)
    DialogResetUsersPasswords.show()
    sys.exit(app.exec())
