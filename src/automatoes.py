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
    #kitchen
    fr = Device('fridge')
    devices.append(fr)
    st = Device('Stove')
    devices.append(st)
    dw = Device('Dish washer')
    devices.append(dw)
    ow = Device('Oven')
    devices.append(ow)
    mw = Device('Microwave')
    devices.append(mw)
    kl = Device('Kitchen light')
    devices.append(kl)

    #bathroom

    wm = Device('washing machine')
    devices.append(wm)
    dr = Device('Dryer')
    devices.append(dr)
    bl = Device('Bathroom light')
    devices.append(bl)

    #livingroom

    tv = Device('tv')
    devices.append(tv)
    ac = Device('Air condition')
    devices.append(ac)
    ll = Device('Livingroom light')

    #rooms

    lrl = Device('Left room light')
    devices.append(lrl)
    rrl = Device('Right room light')
    devices.append(rrl)
    cp = Device('Computer')
    devices.append(cp)

    return devices

def home_setup():
    devices = devices_setup()
    home = SmartHome(None, devices)
    return home


if __name__ == '__main__':
    run()
