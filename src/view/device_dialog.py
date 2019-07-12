from PyQt5.QtWidgets import QApplication, QDialog, QPushButton, QRadioButton, QComboBox, QGridLayout, QLabel, QLineEdit

class DeviceDialog(QDialog):
    def __init__(self, device):
        super(DeviceDialog, self).__init__()
        self.device = device
        self.setup_components()

    def setup_components(self):
        layout = QGridLayout()
        self.setLayout(layout)
        self.setWindowTitle(self.device.name)
        #layout.addWidget(QLabel(self.device.name), 0, 0, 1, 1)
        layout.addWidget(QLabel('Electirity consumption: ' + str(self.device.elect)), 0, 0, 1, 1)
        layout.addWidget(QLabel('Water consumption: ' + str(self.device.water)), 1, 0, 1, 1)
        layout.addWidget(QLabel('Gas consumption: ' + str(self.device.gas)), 2, 0, 1, 1)

        self.on = QRadioButton()
        layout.addWidget(QLabel("On"), 3, 1, 1, 1)
        layout.addWidget(self.on, 3, 2, 1, 1)
        self.off = QRadioButton()
        layout.addWidget(QLabel("Off"), 3, 3, 1, 1)
        layout.addWidget(self.off, 3, 4, 1, 1)
        if self.device.on:
            self.on.setChecked(True)
            self.off.setChecked(False)
        else:
            self.off.setChecked(True)
            self.on.setChecked(False)
        ok_btn = QPushButton("Ok")
        layout.addWidget(ok_btn, 4, 0, 1, 1)
        ok_btn.clicked.connect(self.ok_action)

    def ok_action(self):
        if self.off.isChecked():
            self.device.on = False
        else:
            self.device.on = True
        self.close()



class DeviceL:
    def __init__(self, name, elect, water, gas):
        self.name = name
        self.elect = elect
        self.water = water
        self.gas = gas
        self.on = True
