from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit
from src.model.bill import ResourceType



class BillDialog(QDialog):
    def __init__(self, unit, home):
        super(BillDialog, self).__init__()
        self.unit = unit
        self.home = home
        self.devices = home.devices
        self.unit_price = self.resources()
        self.setup_components()


    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel("Unit: "),0,0,1,1)
        layout.addWidget(QLabel(self.unit), 0, 1, 1, 1)
        layout.addWidget(QLabel("Unit price:"),1,0,1,1)
        layout.addWidget(QLabel(str(self.unit_price[self.unit])), 1,1,1,1)


        layout.addWidget(QLabel("Total: "), 2, 0, 1, 1)
        total = self.total_price()
        layout.addWidget(QLabel(str(total)),2,1,1,1)

        layout.addWidget(QLabel("Date: 12/7/2019"), 3, 0, 1, 1)
        self.selectButton = QPushButton("Ok")
        layout.addWidget(self.selectButton, 4, 2, 1, 1)
        self.cancelButton = QPushButton("Cancel")
        layout.addWidget(self.cancelButton, 4, 3, 1, 1)
        self.cancelButton.clicked.connect(self.close)
        self.selectButton.clicked.connect(self.hide)


    def resources(self):
        unit_price = {}

        unit_price['Electricity'] = 1
        unit_price['Water'] = 1
        unit_price['Internet'] = 5000
        unit_price['Gas'] = 2

        return unit_price

    def total_price(self):
        total = 0

        for item in self.devices.keys():
            '''
            print(self.devices[item].elec)
            elec_per_hour = self.devices[item].elec
            water_per_hour = self.devices[item].water
            gas_per_hour = self.devices[item].gas

            if(self.unit == 'Electricty'):
                total = total + elec_per_hour*30*24
            elif(self.unit == 'Water'):
                total = total + water_per_hour*30*24
            elif(self.unit == 'Gas'):
                total = total + gas_per_hour*30*24
            '''
            if (self.unit == 'Electricity'):
                total = total + self.devices[item].elect * 30 * 24 * self.unit_price[self.unit]
            elif (self.unit == 'Water'):
                total = total + self.devices[item].water * 30 * 24 * self.unit_price[self.unit]
            elif (self.unit == 'Gas'):
                total = total + self.devices[item].gas * 30 * 24 * self.unit_price[self.unit]
            else:
                total = self.home.monthly_internet
        return total