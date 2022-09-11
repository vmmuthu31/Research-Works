import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets, QtCore
from form import Ui_Form
import sys
import sqlite3, bcrypt
from homepage import Ui_MainWindow
class LoginApp(QtWidgets.QWidget, Ui_Form):
    def changeForm(self):
        if self.side.isChecked():
            print("clicked")
            self.log.hide()
            self.reg.show()
            self.side.setText("<")
    def changeForm_(self):
        print("click")
        self.log.show()
        self.reg.hide()
        self.side_.setText(">")
    def Check_inputs(self,password,email):
        if ('@' in email):
            special_char = '[!%^&*()<>?/\|}{~:]'
            for i in special_char:
                if( i in password ):
                    return False
        else:
            return False
        return True
  
    def signin(self):
        def set_id():
            count = 0
            quary = conn.execute(f"""select * from COMPANY""")
            for i in quary:
                count = count + 1
            return count+1
        conn = sqlite3.connect('test.sqlite')
        name = self.lineEdit_13.text()
        email = self.lineEdit_12.text()
        password = (self.lineEdit_15.text()).upper()
        con_password = self.lineEdit_16.text()
        if self.Check_inputs(password,email):
            org = self.lineEdit_17.text()
            if(password == con_password):
                try:
                    bytes = password.encode("utf-8")
                    salt = bcrypt.gensalt()
                    hash = bcrypt.hashpw(bytes, salt)
                    conn.execute(f"""INSERT INTO COMPANY (ID,NAME,EMAIL,PASS,ORG) VALUES (?,?,?,?,?)""",(set_id(),name,email,hash,org))
                    conn.commit()
                    conn.close()
                except:
                    print("email already exist....")
            else:
                print("did not same")
        else:
            print("please check inputs")
    def login(self):
        worng = True
        email = self.lineEdit.text()
        password = self.lineEdit_2.text()
        conn = sqlite3.connect('test.sqlite')
        format = f"""select PASS from COMPANY WHERE EMAIL = '{email}' """
        quary = conn.execute(format)
        out = list(quary.fetchall())
        print(out[0][0])
        if bcrypt.checkpw(password.encode('utf-8'),out[0][0]):
            self.sub_window = SubWindow()
             # Button Event
            self.sub_window.show
        else:
            print("wrong")
                
    def __init__(self):
        super(LoginApp, self).__init__()
        self.setupUi(self)
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)
        self.label.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.label_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=0, yOffset=0))
        self.logbtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.regbtn.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(blurRadius=25, xOffset=3, yOffset=3))
        self.reg.hide()
        self.side.clicked.connect(self.changeForm)
        self.side_.clicked.connect(self.changeForm_)
        self.regbtn.clicked.connect(self.signin)
        self.logbtn.clicked.connect(self.login)

class SubWindow(QWidget):
     def __init__(self):
         super(SubWindow, self).__init__()
         self.resize(400, 300)

         # Label
         self.label = QLabel(self)
         self.label.setGeometry(0, 0, 400, 300)
         self.label.setText('Sub Window')
         self.label.setAlignment(Qt.AlignCenter)
         self.label.setStyleSheet('font-size:40px')
class LoginApp1(QtWidgets.QWidget, Ui_MainWindow):
   def __init__(self):
         super(LoginApp1, self).__init__()
         self.resize(400, 300)
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    Form = LoginApp()
    Form.show()
    sys.exit(app.exec_())
