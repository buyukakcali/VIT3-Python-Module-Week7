# Form implementation generated from reading ui file 'UI_Files/about_coder_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_DialogAboutCoder(object):
    def setupUi(self, DialogAboutCoder):
        DialogAboutCoder.setObjectName("DialogAboutCoder")
        DialogAboutCoder.resize(250, 336)
        DialogAboutCoder.setMinimumSize(QtCore.QSize(250, 336))
        DialogAboutCoder.setMaximumSize(QtCore.QSize(250, 340))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/logo1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        DialogAboutCoder.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(parent=DialogAboutCoder)
        self.buttonBox.setGeometry(QtCore.QRect(10, 280, 231, 41))
        self.buttonBox.setStyleSheet("background-color: rgb(0, 0, 0, 0);\n"
"")
        self.buttonBox.setOrientation(QtCore.Qt.Orientation.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.StandardButton.Ok)
        self.buttonBox.setCenterButtons(True)
        self.buttonBox.setObjectName("buttonBox")
        self.labelFullNme = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelFullNme.setGeometry(QtCore.QRect(20, 160, 225, 16))
        self.labelFullNme.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelFullNme.setObjectName("labelFullNme")
        self.labelPic = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelPic.setGeometry(QtCore.QRect(20, 15, 111, 111))
        self.labelPic.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelPic.setText("")
        self.labelPic.setPixmap(QtGui.QPixmap("UI_Files\\pictures/coder.png"))
        self.labelPic.setScaledContents(True)
        self.labelPic.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.labelPic.setObjectName("labelPic")
        self.labelCopyright = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelCopyright.setGeometry(QtCore.QRect(150, 15, 91, 91))
        self.labelCopyright.setStyleSheet("QLabel {\n"
"    color: red;\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelCopyright.setAlignment(QtCore.Qt.AlignmentFlag.AlignRight|QtCore.Qt.AlignmentFlag.AlignTop|QtCore.Qt.AlignmentFlag.AlignTrailing)
        self.labelCopyright.setObjectName("labelCopyright")
        self.labelEmail = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelEmail.setGeometry(QtCore.QRect(65, 185, 180, 20))
        self.labelEmail.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.labelEmail.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelEmail.setWordWrap(True)
        self.labelEmail.setOpenExternalLinks(True)
        self.labelEmail.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.labelEmail.setObjectName("labelEmail")
        self.labelGithubLink = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelGithubLink.setGeometry(QtCore.QRect(65, 210, 180, 16))
        self.labelGithubLink.setCursor(QtGui.QCursor(QtCore.Qt.CursorShape.PointingHandCursor))
        self.labelGithubLink.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelGithubLink.setOpenExternalLinks(True)
        self.labelGithubLink.setTextInteractionFlags(QtCore.Qt.TextInteractionFlag.LinksAccessibleByKeyboard|QtCore.Qt.TextInteractionFlag.LinksAccessibleByMouse|QtCore.Qt.TextInteractionFlag.TextBrowserInteraction|QtCore.Qt.TextInteractionFlag.TextSelectableByKeyboard|QtCore.Qt.TextInteractionFlag.TextSelectableByMouse)
        self.labelGithubLink.setObjectName("labelGithubLink")
        self.labelEducation = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelEducation.setGeometry(QtCore.QRect(20, 235, 225, 16))
        self.labelEducation.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelEducation.setObjectName("labelEducation")
        self.labelGithub = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelGithub.setGeometry(QtCore.QRect(20, 210, 49, 16))
        self.labelGithub.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelGithub.setObjectName("labelGithub")
        self.labelMail = QtWidgets.QLabel(parent=DialogAboutCoder)
        self.labelMail.setGeometry(QtCore.QRect(20, 185, 41, 16))
        self.labelMail.setStyleSheet("QLabel {\n"
"    background-color: rgb(0, 0, 0, 0);\n"
"}")
        self.labelMail.setObjectName("labelMail")
        self.labelFullNme.raise_()
        self.buttonBox.raise_()
        self.labelPic.raise_()
        self.labelCopyright.raise_()
        self.labelEmail.raise_()
        self.labelGithubLink.raise_()
        self.labelEducation.raise_()
        self.labelGithub.raise_()
        self.labelMail.raise_()

        self.retranslateUi(DialogAboutCoder)
        self.buttonBox.accepted.connect(DialogAboutCoder.accept) # type: ignore
        self.buttonBox.rejected.connect(DialogAboutCoder.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(DialogAboutCoder)

    def retranslateUi(self, DialogAboutCoder):
        _translate = QtCore.QCoreApplication.translate
        DialogAboutCoder.setWindowTitle(_translate("DialogAboutCoder", "About Coder"))
        self.labelFullNme.setText(_translate("DialogAboutCoder", "Name  : M. Fatih BUYUKAKCALI"))
        self.labelCopyright.setText(_translate("DialogAboutCoder", "© 2024"))
        self.labelEmail.setText(_translate("DialogAboutCoder", "buyukakcali@gmail.com"))
        self.labelGithubLink.setText(_translate("DialogAboutCoder", "https://github.com/buyukakcali/"))
        self.labelEducation.setText(_translate("DialogAboutCoder", "Computer Engineer 2013"))
        self.labelGithub.setText(_translate("DialogAboutCoder", "Github :"))
        self.labelMail.setText(_translate("DialogAboutCoder", "Mail     :"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    DialogAboutCoder = QtWidgets.QDialog()
    ui = Ui_DialogAboutCoder()
    ui.setupUi(DialogAboutCoder)
    DialogAboutCoder.show()
    sys.exit(app.exec())
