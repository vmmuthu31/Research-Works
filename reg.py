# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reg.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Login(object):
    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(626, 473)
        self.widget = QtWidgets.QWidget(Login)
        self.widget.setGeometry(QtCore.QRect(0, -10, 721, 471))
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
        self.label_2.setGeometry(QtCore.QRect(-20, 0, 351, 461))
        self.label_2.setStyleSheet("background-color:rgba(0, 0, 0, 80);\n"
"border-top-left-radius: 50px; background-image: url(\'https://formdynamics.io/wp-content/uploads/2020/03/3d-model-1024x722.jpeg\');")
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("images/3d-model-1024x722.jpeg"))
        self.label_2.setObjectName("label_2")
        self.label_6 = QtWidgets.QLabel(self.widget)
        self.label_6.setGeometry(QtCore.QRect(50, 130, 230, 130))
        self.label_6.setStyleSheet("background-color:rgba(0, 0, 0, 75);")
        self.label_6.setText("")
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.widget)
        self.label_7.setGeometry(QtCore.QRect(60, 150, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_7.setFont(font)
        self.label_7.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.widget)
        self.label_8.setGeometry(QtCore.QRect(70, 190, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_8.setFont(font)
        self.label_8.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_8.setObjectName("label_8")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setGeometry(QtCore.QRect(330, 10, 281, 451))
        self.label_3.setStyleSheet("background-color:rgba(255, 255, 255, 255);\n"
"border-bottom-right-radius: 50px;")
        self.label_3.setText("")
        self.label_3.setObjectName("label_3")
        self.widget_8 = QtWidgets.QWidget(self.widget)
        self.widget_8.setGeometry(QtCore.QRect(330, 0, 281, 461))
        self.widget_8.setObjectName("widget_8")
        self.label_44 = QtWidgets.QLabel(self.widget_8)
        self.label_44.setGeometry(QtCore.QRect(50, 30, 121, 41))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_44.setFont(font)
        self.label_44.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_44.setText("")
        self.label_44.setObjectName("label_44")
        self.label_9 = QtWidgets.QLabel(self.widget_8)
        self.label_9.setGeometry(QtCore.QRect(70, 40, 141, 40))
        font = QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        font.setWeight(75)
        self.label_9.setFont(font)
        self.label_9.setStyleSheet("color:rgba(0, 0, 0, 200);")
        self.label_9.setObjectName("label_9")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_4.setGeometry(QtCore.QRect(30, 90, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_4.setFont(font)
        self.lineEdit_4.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_3.setGeometry(QtCore.QRect(30, 140, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_3.setFont(font)
        self.lineEdit_3.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_6.setGeometry(QtCore.QRect(30, 190, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_6.setFont(font)
        self.lineEdit_6.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_6.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.lineEdit_7 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_7.setGeometry(QtCore.QRect(30, 240, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_7.setFont(font)
        self.lineEdit_7.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_7.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.widget_8)
        self.lineEdit_5.setGeometry(QtCore.QRect(30, 290, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.lineEdit_5.setFont(font)
        self.lineEdit_5.setStyleSheet("background-color:rgba(0, 0, 0, 0);\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"padding-bottom:7px;")
        self.lineEdit_5.setEchoMode(QtWidgets.QLineEdit.Normal)
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.pushButton = QtWidgets.QPushButton(self.widget_8)
        self.pushButton.setGeometry(QtCore.QRect(30, 340, 211, 40))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_7 = QtWidgets.QPushButton(self.widget_8)
        self.pushButton_7.setGeometry(QtCore.QRect(210, 390, 30, 40))
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
        self.label_4 = QtWidgets.QLabel(self.widget_8)
        self.label_4.setGeometry(QtCore.QRect(50, 400, 151, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.label_4.setFont(font)
        self.label_4.setObjectName("label_4")
        self.label_42 = QtWidgets.QLabel(Login)
        self.label_42.setGeometry(QtCore.QRect(60, 630, 220, 50))
        font = QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.label_42.setFont(font)
        self.label_42.setStyleSheet("color:rgba(255, 255, 255, 170);")
        self.label_42.setObjectName("label_42")
        self.label_41 = QtWidgets.QLabel(Login)
        self.label_41.setGeometry(QtCore.QRect(60, 590, 180, 40))
        font = QtGui.QFont()
        font.setPointSize(22)
        font.setBold(True)
        font.setWeight(75)
        self.label_41.setFont(font)
        self.label_41.setStyleSheet("color:rgba(255, 255, 255, 200);")
        self.label_41.setObjectName("label_41")

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "Futaucon"))
        self.label_7.setText(_translate("Login", "Futaucon"))
        self.label_8.setText(_translate("Login", "3D Model Generation"))
        self.label_9.setText(_translate("Login", "Register"))
        self.lineEdit_4.setPlaceholderText(_translate("Login", "  First Name"))
        self.lineEdit_3.setPlaceholderText(_translate("Login", "  Email Address"))
        self.lineEdit_6.setPlaceholderText(_translate("Login", "  Password"))
        self.lineEdit_7.setPlaceholderText(_translate("Login", "  Confirm Password"))
        self.lineEdit_5.setPlaceholderText(_translate("Login", "    Organization"))
        self.pushButton.setText(_translate("Login", "Register"))
        self.pushButton_7.setText(_translate("Login", ">"))
        self.label_4.setText(_translate("Login", "Already Registered?"))
        self.label_42.setText(_translate("Login", "3D Model Generation"))
        self.label_41.setText(_translate("Login", "Futaucon"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QWidget()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())

