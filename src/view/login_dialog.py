from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit



class LoginDialog(QDialog):
    def __init__(self):
        super(LoginDialog, self).__init__()
        self.username = ""
        self.password = ""
        self.wrong_label = QLabel("Wrong login")
        self.exit = False
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
        self.cancelButton.clicked.connect(self.cancel_action)
        self.selectButton.clicked.connect(self.confirmed)

        layout.addWidget(self.wrong_label)
        self.wrong_label.hide()

    def confirmed(self):
        if self.name.text() == "":
            return
        if self.passw.text() == "":
            return
        self.username = self.name.text()
        self.password = self.passw.text()
        self.hide()

    def wrong(self):
        self.wrong_label.setStyleSheet('color: red')
        self.wrong_label.show()

    def cancel_action(self):
        self.exit = True
        self.hide()
