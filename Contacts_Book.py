import sqlite3 
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import * 
from PyQt5 import QtCore
import sys

conn = sqlite3.connect('contacts.db')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS contacts(contact TEXT)")
conn.commit()
conn.close()

class Ui_Contacts(object):
    def setupUi(self, Contacts):
        Contacts.setObjectName("Contacts")
        Contacts.resize(730, 528)
        
        self.AddContact = QtWidgets.QPushButton(Contacts, clicked= lambda: self.addContact())
        self.AddContact.setGeometry(QtCore.QRect(120, 250, 93, 28))
        self.AddContact.setObjectName("AddContact")
        
        self.list_Info = QtWidgets.QListWidget(Contacts)
        self.list_Info.setGeometry(QtCore.QRect(315, 31, 391, 391))
        self.list_Info.setObjectName("list_Info")
        self.FirstName_field = QtWidgets.QLineEdit(Contacts)
        self.FirstName_field.setGeometry(QtCore.QRect(80, 30, 211, 30))
        self.FirstName_field.setObjectName("FirstName_field")
        self.LastName_field = QtWidgets.QLineEdit(Contacts)
        self.LastName_field.setGeometry(QtCore.QRect(80, 70, 211, 30))
        self.LastName_field.setObjectName("LastName_field")
        self.Email_field = QtWidgets.QLineEdit(Contacts)
        self.Email_field.setGeometry(QtCore.QRect(80, 110, 211, 30))
        self.Email_field.setObjectName("Email_field")
        self.Phone_Field = QtWidgets.QLineEdit(Contacts)
        self.Phone_Field.setGeometry(QtCore.QRect(80, 150, 211, 30))
        self.Phone_Field.setObjectName("Phone_Field")
        self.Location_Field = QtWidgets.QLineEdit(Contacts)
        self.Location_Field.setGeometry(QtCore.QRect(80, 190, 211, 30))
        self.Location_Field.setObjectName("Location_Field")
        self.First_label = QtWidgets.QLabel(Contacts)
        self.First_label.setGeometry(QtCore.QRect(4, 30, 71, 20))
        self.First_label.setObjectName("First_label")
        self.Last_lable = QtWidgets.QLabel(Contacts)
        self.Last_lable.setGeometry(QtCore.QRect(4, 70, 71, 20))
        self.Last_lable.setObjectName("Last_lable")
        self.Emaillabel = QtWidgets.QLabel(Contacts)
        self.Emaillabel.setGeometry(QtCore.QRect(10, 110, 71, 20))
        self.Emaillabel.setObjectName("Emaillabel")
        self.PhoneLabel = QtWidgets.QLabel(Contacts)
        self.PhoneLabel.setGeometry(QtCore.QRect(10, 150, 71, 20))
        self.PhoneLabel.setObjectName("PhoneLabel")
        self.LocLabel = QtWidgets.QLabel(Contacts)
        self.LocLabel.setGeometry(QtCore.QRect(10, 190, 71, 20))
        self.LocLabel.setObjectName("LocLabel")

        self.retranslateUi(Contacts)
        QtCore.QMetaObject.connectSlotsByName(Contacts)
        self.grab_all()

    def grab_all(self):
        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        cur.execute("SELECT * FROM contacts")
        records = cur.fetchall()
        conn.commit()
        conn.close()

        for record in records:
            self.list_Info.addItem(str(record[0]))

        # Add Contact funtion
    def addContact(self):
        # Grab content 
        fname = self.FirstName_field.text()
        lname = self.LastName_field.text()
        email = self.Email_field.text()
        phone = self.Phone_Field.text()
        loc = self.Location_Field.text()

        layout = str(f'{fname} | {lname} | {email} | {phone} | {loc}')
        # Add filds to list
        self.list_Info.addItem(layout)

        conn = sqlite3.connect('contacts.db')
        cur = conn.cursor()
        
        items = []
        for index in range(self.list_Info.count()):
            items.append(self.list_Info.item(index))

        for  item in items:
            cur.execute("INSERT INTO contacts VALUES (:contact)", 
            {
                'contact': item.text(),
            }
            )
        conn.commit()
        conn.close()

    def retranslateUi(self, Contacts):
        _translate = QtCore.QCoreApplication.translate
        Contacts.setWindowTitle(_translate("Contacts", "Contacts Book"))
        self.AddContact.setText(_translate("Contacts", "Add Contact"))
        self.First_label.setText(_translate("Contacts", " First Name "))
        self.Last_lable.setText(_translate("Contacts", " Last Name "))
        self.Emaillabel.setText(_translate("Contacts", "Email"))
        self.PhoneLabel.setText(_translate("Contacts", "Phone"))
        self.LocLabel.setText(_translate("Contacts", "Location"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Contacts = QtWidgets.QDialog()
    ui = Ui_Contacts()
    ui.setupUi(Contacts)
    Contacts.show()
    sys.exit(app.exec_())