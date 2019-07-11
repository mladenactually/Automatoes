from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit

class DeviceDialog(QDialog):
    def __init__(self, device):
        super(DeviceDialog, self).__init__()
        self.device = device
        self.setup_components()

    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        layout.addWidget(QLabel(self.device.name), 0, 0, 1, 1)
        layout.addWidget(QLabel('Electirity consumption: ' + str(self.device.elect)), 1, 0, 1, 1)
        layout.addWidget(QLabel('Water consumption: ' + str(self.device.water)), 2, 0, 1, 1)
        layout.addWidget(QLabel('Gas consumption: ' + str(self.device.gas)), 3, 0, 1, 1)

        self.on = QRadioButton()
        layout.addWidget(QLabel("On"), 4, 0, 1, 1)
        layout.addWidget(self.on, 4, 1, 1, 1)
        self.offButton = QRadioButton()
        layout.addWidget(QLabel("Off"), 4, 2, 1, 1)
        layout.addWidget(self.offButton, 4, 3, 1, 1)


class DeviceL:
    def __init__(self, name, elect, water, gas):
        self.name = name
        self.elect = elect
        self.water = water
        self.gas = gas
