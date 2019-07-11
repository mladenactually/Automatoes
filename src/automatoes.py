from sys import argv, exit
from src.model.device import Device, DiscreteScale, ContinuousScale, ToggleSettings, SecuritySettings, ResourceAware
from src.model.smarthome import SmartHome
from PyQt5.QtWidgets import QApplication

from src.view.mainwindow import MainWindow


def run():
    app = QApplication(argv)
    app.home = home_setup()
    window = MainWindow(app)
    window.show()
    exit(app.exec_())


def devices_setup():
    devices = []
    wm = Device('washing machine')
    devices.append(wm)

    return devices

def home_setup():
    devices = devices_setup()
    home = SmartHome(None, devices)
    return home


if __name__ == '__main__':
    run()
