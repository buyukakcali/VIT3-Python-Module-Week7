# Form implementation generated from reading ui file 'UI_Files/interviews_ui.ui'
#
# Created by: PyQt6 UI code generator 6.7.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_FormInterviews(object):
    def setupUi(self, FormInterviews):
        FormInterviews.setObjectName("FormInterviews")
        FormInterviews.resize(900, 500)
        FormInterviews.setMinimumSize(QtCore.QSize(840, 500))
        FormInterviews.setMaximumSize(QtCore.QSize(16777215, 16777215))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("UI_Files\\pictures/logo1.ico"), QtGui.QIcon.Mode.Normal, QtGui.QIcon.State.Off)
        FormInterviews.setWindowIcon(icon)
        FormInterviews.setStyleSheet("background-color: qlineargradient(spread:pad, x1:0.489, y1:1, x2:0.494, y2:0, stop:0 rgba(71, 71, 71, 255), stop:1 rgba(255, 255, 255, 255));")
        self.gridLayout = QtWidgets.QGridLayout(FormInterviews)
        self.gridLayout.setObjectName("gridLayout")
        self.pushButtonInterviewedApplicants = QtWidgets.QPushButton(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonInterviewedApplicants.sizePolicy().hasHeightForWidth())
        self.pushButtonInterviewedApplicants.setSizePolicy(sizePolicy)
        self.pushButtonInterviewedApplicants.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonInterviewedApplicants.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButtonInterviewedApplicants.setFont(font)
        self.pushButtonInterviewedApplicants.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}")
        self.pushButtonInterviewedApplicants.setObjectName("pushButtonInterviewedApplicants")
        self.gridLayout.addWidget(self.pushButtonInterviewedApplicants, 6, 0, 1, 1)
        self.pushButtonExit = QtWidgets.QPushButton(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonExit.sizePolicy().hasHeightForWidth())
        self.pushButtonExit.setSizePolicy(sizePolicy)
        self.pushButtonExit.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonExit.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonExit.setFont(font)
        self.pushButtonExit.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}")
        self.pushButtonExit.setObjectName("pushButtonExit")
        self.gridLayout.addWidget(self.pushButtonExit, 8, 0, 1, 1)
        self.pushButtonUnassignedApplicants = QtWidgets.QPushButton(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonUnassignedApplicants.sizePolicy().hasHeightForWidth())
        self.pushButtonUnassignedApplicants.setSizePolicy(sizePolicy)
        self.pushButtonUnassignedApplicants.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonUnassignedApplicants.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonUnassignedApplicants.setFont(font)
        self.pushButtonUnassignedApplicants.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}")
        self.pushButtonUnassignedApplicants.setObjectName("pushButtonUnassignedApplicants")
        self.gridLayout.addWidget(self.pushButtonUnassignedApplicants, 4, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.comboBoxFilterOptions = QtWidgets.QComboBox(parent=FormInterviews)
        self.comboBoxFilterOptions.setMinimumSize(QtCore.QSize(300, 0))
        self.comboBoxFilterOptions.setStyleSheet("QComboBox {\n"
"    border-radius : 15px;\n"
"    border: 3px solid rgb(85, 255, 255);\n"
"    background-color: rgba(0, 0, 0,55%);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"\n"
"QComboBox:hover {\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}\n"
"\n"
"QComboBox:focus  {\n"
"  border: 2px solid rgb(162, 0, 0);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"")
        self.comboBoxFilterOptions.setObjectName("comboBoxFilterOptions")
        self.horizontalLayout.addWidget(self.comboBoxFilterOptions, 0, QtCore.Qt.AlignmentFlag.AlignRight)
        self.gridLayout.addLayout(self.horizontalLayout, 2, 4, 1, 2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Policy.Expanding, QtWidgets.QSizePolicy.Policy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 5, 1, 1)
        self.labelPicture = QtWidgets.QLabel(parent=FormInterviews)
        self.labelPicture.setMaximumSize(QtCore.QSize(200, 150))
        self.labelPicture.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.labelPicture.setText("")
        self.labelPicture.setPixmap(QtGui.QPixmap("UI_Files\\pictures/interviews_menu.png"))
        self.labelPicture.setScaledContents(True)
        self.labelPicture.setObjectName("labelPicture")
        self.gridLayout.addWidget(self.labelPicture, 0, 0, 1, 1)
        self.labelLogo = QtWidgets.QLabel(parent=FormInterviews)
        self.labelLogo.setMaximumSize(QtCore.QSize(16777215, 150))
        self.labelLogo.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.labelLogo.setText("")
        self.labelLogo.setPixmap(QtGui.QPixmap("UI_Files\\pictures/logo1.ico"))
        self.labelLogo.setScaledContents(False)
        self.labelLogo.setObjectName("labelLogo")
        self.gridLayout.addWidget(self.labelLogo, 0, 2, 1, 1)
        self.tableWidget = QtWidgets.QTableWidget(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy)
        self.tableWidget.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(170)
        self.gridLayout.addWidget(self.tableWidget, 3, 1, 7, 5)
        self.labelMenu = QtWidgets.QLabel(parent=FormInterviews)
        self.labelMenu.setMinimumSize(QtCore.QSize(380, 0))
        self.labelMenu.setMaximumSize(QtCore.QSize(16777215, 60))
        font = QtGui.QFont()
        font.setFamily("Arial Black")
        font.setPointSize(26)
        font.setBold(True)
        self.labelMenu.setFont(font)
        self.labelMenu.setStyleSheet("background-color: rgba(0, 0, 0,0%);\n"
"color: rgb(71, 84, 88);")
        self.labelMenu.setScaledContents(True)
        self.labelMenu.setObjectName("labelMenu")
        self.gridLayout.addWidget(self.labelMenu, 2, 2, 1, 2)
        self.lineEditSearch = QtWidgets.QLineEdit(parent=FormInterviews)
        self.lineEditSearch.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEditSearch.sizePolicy().hasHeightForWidth())
        self.lineEditSearch.setSizePolicy(sizePolicy)
        self.lineEditSearch.setMinimumSize(QtCore.QSize(150, 35))
        self.lineEditSearch.setMaximumSize(QtCore.QSize(160, 35))
        self.lineEditSearch.setFocusPolicy(QtCore.Qt.FocusPolicy.StrongFocus)
        self.lineEditSearch.setStyleSheet("QLineEdit {\n"
"  border: 2px solid rgb(35, 218, 233);\n"
"  border-radius: 15px;\n"
"  color: #FFF;\n"
"  padding-left: 15px;\n"
"  background-color: rgba(0, 0, 0,55%); \n"
"}\n"
"\n"
"QLineEdit:hover {\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}\n"
"\n"
"QLineEdit:focus  {\n"
"  border: 2px solid rgb(162, 0, 0);\n"
"  background-color: rgb(47, 47, 47);\n"
"}\n"
"")
        self.lineEditSearch.setText("")
        self.lineEditSearch.setObjectName("lineEditSearch")
        self.gridLayout.addWidget(self.lineEditSearch, 3, 0, 1, 1)
        self.label = QtWidgets.QLabel(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Preferred, QtWidgets.QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMinimumSize(QtCore.QSize(0, 100))
        self.label.setMaximumSize(QtCore.QSize(16777215, 100))
        self.label.setStyleSheet("background-color: rgba(0, 0, 0,0%);")
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("UI_Files\\pictures/logo2.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 3, 1, 2)
        self.pushButtonBackMenu = QtWidgets.QPushButton(parent=FormInterviews)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Policy.Fixed, QtWidgets.QSizePolicy.Policy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButtonBackMenu.sizePolicy().hasHeightForWidth())
        self.pushButtonBackMenu.setSizePolicy(sizePolicy)
        self.pushButtonBackMenu.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonBackMenu.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setBold(True)
        self.pushButtonBackMenu.setFont(font)
        self.pushButtonBackMenu.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}")
        self.pushButtonBackMenu.setObjectName("pushButtonBackMenu")
        self.gridLayout.addWidget(self.pushButtonBackMenu, 7, 0, 1, 1)
        self.labelInfo1 = QtWidgets.QLabel(parent=FormInterviews)
        self.labelInfo1.setEnabled(False)
        self.labelInfo1.setMinimumSize(QtCore.QSize(10, 10))
        self.labelInfo1.setMaximumSize(QtCore.QSize(10, 10))
        self.labelInfo1.setText("")
        self.labelInfo1.setObjectName("labelInfo1")
        self.gridLayout.addWidget(self.labelInfo1, 10, 2, 1, 1)
        self.pushButtonAssignedApplicants = QtWidgets.QPushButton(parent=FormInterviews)
        self.pushButtonAssignedApplicants.setMinimumSize(QtCore.QSize(150, 35))
        self.pushButtonAssignedApplicants.setMaximumSize(QtCore.QSize(160, 35))
        font = QtGui.QFont()
        font.setBold(True)
        self.pushButtonAssignedApplicants.setFont(font)
        self.pushButtonAssignedApplicants.setStyleSheet("QPushButton{\n"
"    border-radius : 15px;\n"
"    background-color : rgb(25, 200, 200);\n"
"    color: rgb(255, 255, 255);\n"
"}\n"
"QPushButton:hover{\n"
"    background-color: rgb(20, 135, 135);\n"
"    border: 2px solid rgb(255, 80, 0);\n"
"}")
        self.pushButtonAssignedApplicants.setObjectName("pushButtonAssignedApplicants")
        self.gridLayout.addWidget(self.pushButtonAssignedApplicants, 5, 0, 1, 1)
        self.lineEditSearch.raise_()
        self.labelPicture.raise_()
        self.labelLogo.raise_()
        self.tableWidget.raise_()
        self.label.raise_()
        self.pushButtonUnassignedApplicants.raise_()
        self.pushButtonInterviewedApplicants.raise_()
        self.pushButtonBackMenu.raise_()
        self.pushButtonExit.raise_()
        self.labelInfo1.raise_()
        self.labelMenu.raise_()
        self.pushButtonAssignedApplicants.raise_()

        self.retranslateUi(FormInterviews)
        QtCore.QMetaObject.connectSlotsByName(FormInterviews)

    def retranslateUi(self, FormInterviews):
        _translate = QtCore.QCoreApplication.translate
        FormInterviews.setWindowTitle(_translate("FormInterviews", "INTERVIEWS"))
        self.pushButtonInterviewedApplicants.setText(_translate("FormInterviews", "Interviewed Applicants"))
        self.pushButtonExit.setText(_translate("FormInterviews", "Exit"))
        self.pushButtonUnassignedApplicants.setText(_translate("FormInterviews", "Unassigned Apllicants"))
        self.labelMenu.setText(_translate("FormInterviews", "INTERVIEWS MENU"))
        self.lineEditSearch.setPlaceholderText(_translate("FormInterviews", "      Name or Surname"))
        self.pushButtonBackMenu.setText(_translate("FormInterviews", "Back Menu"))
        self.pushButtonAssignedApplicants.setText(_translate("FormInterviews", "Assigned Applicants"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    FormInterviews = QtWidgets.QWidget()
    ui = Ui_FormInterviews()
    ui.setupUi(FormInterviews)
    FormInterviews.show()
    sys.exit(app.exec())
