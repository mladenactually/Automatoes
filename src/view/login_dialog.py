from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit
from PyQt5.QtCore import Qt
from sys import argv, exit

class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.username = ""
        self.password = ""
        self.setup_components()

    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Username: "), 0, 0, 1, 1)
        self.name = QLineEdit()
        layout.addWidget(self.name, 0, 1, 1, 1)

        layout.addWidget(QLabel("Password"), 2, 0, 1, 1)
        self.passw = QLineEdit()
        layout.addWidget(self.passw, 2, 1, 1, 1)
        self.selectButton = QPushButton("Ok")
        layout.addWidget(self.selectButton, 4, 2, 1, 1)
        self.cancelButton = QPushButton("Cancel", self)
        layout.addWidget(self.cancelButton, 4, 3, 1, 1)
        #self.makeActions()
