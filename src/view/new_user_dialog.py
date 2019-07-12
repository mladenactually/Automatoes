from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit
import os


class NewUserDialog(QDialog):
    def __init__(self):
        super(NewUserDialog, self).__init__()
        self.name = ""
        self.lastname = ""
        self.username = ""
        self.password = ""
        self.setup_components()

    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Name: "),0,0,1,1)
        self.nameInput = QLineEdit()
        layout.addWidget(self.nameInput, 0, 1, 1, 1)
        layout.addWidget(QLabel("Last name:"),1,0,1,1)
        self.lastnameInput = QLineEdit()
        layout.addWidget(self.lastnameInput, 1,1,1,1)


        layout.addWidget(QLabel("Username: "), 2, 0, 1, 1)
        self.usernameInput = QLineEdit()
        layout.addWidget(self.usernameInput,2,1,1,1)

        layout.addWidget(QLabel("Password:"), 3, 0, 1, 1)
        self.passwordInput = QLineEdit()
        layout.addWidget(self.passwordInput, 3, 1, 1, 1)
        self.selectButton = QPushButton("Ok")
        layout.addWidget(self.selectButton, 4, 2, 1, 1)
        self.cancelButton = QPushButton("Cancel", self)
        layout.addWidget(self.cancelButton, 4, 3, 1, 1)
        self.cancelButton.clicked.connect(self.close)
        self.selectButton.clicked.connect(self.confirmed)

    def confirmed(self):
        self.name = self.nameInput.text()
        self.lastname = self.lastnameInput.text()
        self.username = self.usernameInput.text()
        self.password = self.passwordInput.text()
        self.add_new()
        self.hide()

    def add_new(self):
        if self.lastname != "" and self.name != "" and self.username != "" and self.password != "":
            file = open(".." + os.sep + "Data" + os.sep + 'user_data.txt', 'a')
            file.write(self.name + "|" + self.lastname + "|" + self.username + "|" + self.password + "\n")
            file.close()