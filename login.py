# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'login.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Register(object):
    def setupUi(self, Register):
        Register.setObjectName("Register")
        Register.resize(621, 477)
        self.widget = QtWidgets.QWidget(Register)
        self.widget.setGeometry(QtCore.QRect(0, 0, 641, 511))
        self.widget.setStyleSheet("QPushButton#pushButton, #pushButton_6, #pushButton_7{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(11, 131, 120, 219), stop:1 rgba(85, 98, 112, 226));\n"
"    color:rgba(255, 255, 255, 210);\n"
"    border-radius:5px;\n"
"}\n"
"\n"
"QPushButton#pushButton:hover, #pushButton_6:hover, #pushButton_7:hover{\n"
"    background-color: qlineargradient(spread:pad, x1:0, y1:0.505682, x2:1, y2:0.477, stop:0 rgba(150, 123, 111, 219), stop:1 rgba(85, 81, 84, 226));\n"
"}\n"
"\n"
"QPushButton#pushButton:pressed, #pushButton_6:pressed, #pushButton_7:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    background-color:rgba(150, 123, 111, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2, #pushButton_3, #pushButton_4, #pushButton_5{\n"
"    background-color: rgba(0, 0, 0, 0);\n"
"    color:rgba(85, 98, 112, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:hover, #pushButton_3:hover, #pushButton_4:hover, #pushButton_5:hover{\n"
"    color: rgba(131, 96, 53, 255);\n"
"}\n"
"\n"
"QPushButton#pushButton_2:pressed, #pushButton_3:pressed, #pushButton_4:pressed, #pushButton_5:pressed{\n"
"    padding-left:5px;\n"
"    padding-top:5px;\n"
"    color:rgba(91, 88, 53, 255);\n"
"}\n"
"\n"
"")
        self.widget.setObjectName("widget")
        self.label = QtWidgets.QLabel(self.widget)
        self.label.setGeometry(QtCore.QRect(40, 30, 280, 430))
        self.label.setStyleSheet("border-image: url(:/images/background.jpg);\n"
"border-top-left-radius: 50px;")
        self.label.setText("")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.widget)
        self.label_2.setGeometry(QtCore.QRect(-20, 0, 351, 451))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px; background-image: url(\'https://formdynamics.io/wp-content/uploads/2020/03/3d-model-1024x722.jpeg\');")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("../3d-model-1024x722.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(40, 100, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(50, 120, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(50, 160, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 0, 281, 451))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget_2 = QtWidgets.QWidget(self.widget)
        self.widget_2.setGeometry(QtCore.QRect(350, 0, 261, 451))
        self.widget_2.setObjectName("widget_2")
        self.label_4 = QtWidgets.QLabel(self.widget_2)
        self.label_4.setGeometry(QtCore.QRect(60, 50, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_4.setFont(font)
        self.label_4.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_4.setObjectName("label_4")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit_2.setGeometry(QtCore.QRect(30, 180, 181, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_2.setFont(font)
        self.lineEdit_2.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.widget_2)
        self.lineEdit.setGeometry(QtCore.QRect(30, 120, 181, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit.setFont(font)
        self.lineEdit.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.pushButton = QtWidgets.QPushButton(self.widget_2)
        self.pushButton.setGeometry(QtCore.QRect(30, 250, 190, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.label_5 = QtWidgets.QLabel(self.widget_2)
        self.label_5.setGeometry(QtCore.QRect(60, 330, 181, 21))
        self.label_5.setStyleSheet("color:rgba(0, 0, 0, 210);font-size:14px;")
        self.label_5.setObjectName("label_5")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_2)
        self.pushButton_7.setGeometry(QtCore.QRect(180, 320, 30, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_7.setFont(font)
        self.pushButton_7.setStyleSheet("border-radius:0px;\n"
"border-top-right-radius:15px;\n"
"border-bottom-right-radius:15px;")
        self.pushButton_7.setCheckable(True)
        self.pushButton_7.setObjectName("pushButton_7")

        self.retranslateUi(Register)
        QtCore.QMetaObject.connectSlotsByName(Register)

    def retranslateUi(self, Register):
        _translate = QtCore.QCoreApplication.translate
        Register.setWindowTitle(_translate("Register", "Futaucon"))
        self.label_7.setText(_translate("Register", "Futaucon"))
        self.label_8.setText(_translate("Register", "3D Model Generation"))
        self.label_4.setText(_translate("Register", "Log In"))
        self.lineEdit_2.setPlaceholderText(_translate("Register", "  Password"))
        self.lineEdit.setPlaceholderText(_translate("Register", "  User Name"))
        self.pushButton.setText(_translate("Register", "L o g  I n"))
        self.label_5.setText(_translate("Register", "Forgot Password?"))
        self.pushButton_7.setText(_translate("Register", ">"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Register = QtWidgets.QDialog()
    ui = Ui_Register()
    ui.setupUi(Register)
    Register.show()
    sys.exit(app.exec_())

