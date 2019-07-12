from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit
from src.model.bill import ResourceType



class BillDialog(QDialog):
    def __init__(self, unit, home):
        super(BillDialog, self).__init__()
        self.unit = unit
        self.devices = home.devices
        self.home = home
        self.setup_components()
        self.unit_price = self.resources()

    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Unit: "),0,0,1,1)
        layout.addWidget(QLabel(self.unit), 0, 1, 1, 1)
        layout.addWidget(QLabel("Unit price:"),1,0,1,1)
        layout.addWidget(str(self.unit_price[self.unit]), 1,1,1,1)


        layout.addWidget(QLabel("Total: "), 2, 0, 1, 1)
        layout.addWidget(str(self.total_price()),2,1,1,1)

        layout.addWidget(QLabel("Date: 12/7/2019"), 3, 0, 1, 1)
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
        self.hide()

    def resources(self):
        unit_price = {}

        unit_price['Electricity'] = 150
        unit_price['Water'] = 100
        unit_price['Internet'] = 2100
        unit_price['Gas'] = 220

        return unit_price

    def total_price(self):
        total = 0

        for item in self.devices.keys():
            elec_per_hour = self.devices[item].elec
            water_per_hour = self.devices[item].water
            gas_per_hour = self.devices[item].gas

            if(self.unit == 'Electricty'):
                total = total + elec_per_hour*30*24
            elif(self.unit == 'Water'):
                total = total + water_per_hour*30*24
            elif(self.unit == 'Gas'):
                total = total + gas_per_hour*30*24

        return total