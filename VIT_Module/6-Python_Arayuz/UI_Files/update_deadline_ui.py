# Form implementation generated from reading ui file 'UI_Files/update_deadline_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogSetDeadline(object):
    def setupUi(self, DialogSetDeadline):
        DialogSetDeadline.setObjectName("DialogSetDeadline")
        DialogSetDeadline.resize(293, 371)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/logo1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DialogSetDeadline.setWindowIcon(icon)
        DialogSetDeadline.setStyleSheet("background-color: rgb(255, 255, 127);\n"
"QToolTip { background-color: yellow; color: black; border: 1px solid black;}")
        self.dateTimeEdit = QtWidgets.QDateTimeEdit(parent=DialogSetDeadline)
        self.dateTimeEdit.setGeometry(QtCore.QRect(40, 250, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.dateTimeEdit.setFont(font)
        self.dateTimeEdit.setStyleSheet("QDateTimeEdit {\n"
"    color: rgb(255, 255, 255);\n"
"    selection-background-color: rgb(255, 0, 0);\n"
"    background-color: rgb(102, 112, 255);\n"
"}\n"
"")
        self.dateTimeEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Language.Turkish, QtCore.QLocale.Country.Turkey))
        self.dateTimeEdit.setInputMethodHints(QtCore.Qt.InputMethodHint.ImhDate|QtCore.Qt.InputMethodHint.ImhPreferNumbers|QtCore.Qt.InputMethodHint.ImhTime)
        self.dateTimeEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateTimeEdit.setObjectName("dateTimeEdit")
        self.labelCase = QtWidgets.QLabel(parent=DialogSetDeadline)
        self.labelCase.setGeometry(QtCore.QRect(10, 200, 271, 22))
        self.labelCase.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setUnderline(True)
        self.labelCase.setFont(font)
        self.labelCase.setStyleSheet("QLabel { \n"
"    color: black;\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelCase.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelCase.setObjectName("labelCase")
        self.labelPicture = QtWidgets.QLabel(parent=DialogSetDeadline)
        self.labelPicture.setGeometry(QtCore.QRect(1, 1, 291, 181))
        self.labelPicture.setStyleSheet("QLabel {\n"
"    border-radius : 8px;\n"
"    background-color: red;\n"
"}")
        self.labelPicture.setText("")
        self.labelPicture.setPixmap(QtGui.QPixmap("UI_Files\\pictures/deadline_pic.png"))
        self.labelPicture.setScaledContents(True)
        self.labelPicture.setObjectName("labelPicture")
        self.pushButtonSetDeadline = QtWidgets.QPushButton(parent=DialogSetDeadline)
        self.pushButtonSetDeadline.setGeometry(QtCore.QRect(70, 320, 150, 30))
        self.pushButtonSetDeadline.setMinimumSize(QtCore.QSize(150, 30))
        self.pushButtonSetDeadline.setMaximumSize(QtCore.QSize(150, 30))
        self.pushButtonSetDeadline.setMouseTracking(True)
        self.pushButtonSetDeadline.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.pushButtonSetDeadline.setStyleSheet("QPushButton{\n"
"    border-radius : 7px;\n"
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
        self.pushButtonSetDeadline.setObjectName("pushButtonSetDeadline")
        self.dateTimeEdit.raise_()
        self.labelCase.raise_()
        self.pushButtonSetDeadline.raise_()
        self.labelPicture.raise_()

        self.retranslateUi(DialogSetDeadline)
        QtCore.QMetaObject.connectSlotsByName(DialogSetDeadline)
        DialogSetDeadline.setTabOrder(self.dateTimeEdit, self.pushButtonSetDeadline)

    def retranslateUi(self, DialogSetDeadline):
        _translate = QtCore.QCoreApplication.translate
        DialogSetDeadline.setWindowTitle(_translate("DialogSetDeadline", "Set Deadline"))
        self.labelCase.setText(_translate("DialogSetDeadline", "Set the Project Homework Deadline"))
        self.pushButtonSetDeadline.setText(_translate("DialogSetDeadline", "Set Deadline"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogSetDeadline = QtWidgets.QDialog()
    ui = Ui_DialogSetDeadline()
    ui.setupUi(DialogSetDeadline)
    DialogSetDeadline.show()
    sys.exit(app.exec())
