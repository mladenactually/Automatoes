from sys import argv, exit
import os
from src.view.device_dialog import DeviceL
from src.model.smarthome import SmartHome
from PyQt5.QtWidgets import QApplication
from src.view.login_dialog import LoginDialog
from src.view.mainwindow import MainWindow


def run():
    user_data = load_user_data()
    app = QApplication(argv)
    dialog = LoginDialog()
    dialog.show()
    dialog.exec_()

    if login(user_data, dialog.username, dialog.password):
        app.home = home_setup()

        window = MainWindow(app)
        window.show()
    exit(app.exec_())


def devices_setup():
    devices = []
    # kitchen
    fr = DeviceL('fridge', 100, 0, 0)
    devices.append(fr)
    st = DeviceL('Stove')
    devices.append(st)
    dw = DeviceL('Dish washer')
    devices.append(dw)
    ow = DeviceL('Oven')
    devices.append(ow)
    mw = DeviceL('Microwave')
    devices.append(mw)
    kl = DeviceL('Kitchen light')
    devices.append(kl)

    # bathroom

    wm = DeviceL('washing machine')
    devices.append(wm)
    dr = DeviceL('Dryer')
    devices.append(dr)
    bl = DeviceL('Bathroom light')
    devices.append(bl)

    # livingroom

    tv = DeviceL('tv')
    devices.append(tv)
    ac = DeviceL('Air condition')
    devices.append(ac)
    ll = DeviceL('Livingroom light')

    # rooms

    lrl = DeviceL('Left room light')
    devices.append(lrl)
    rrl = DeviceL('Right room light')
    devices.append(rrl)
    cp = DeviceL('Computer')
    devices.append(cp)

    return devices

def home_setup():
    devices = devices_setup()
    home = SmartHome(None, devices)
    return home


def login(user_data, username, password):
    if username in user_data:
        if user_data[username] == password:
            return True
        else:
            return False
    else:
        return False

def logout():
    pass

def load_user_data():
    file = open(".." + os.sep + "Data" + os.sep +'user_data.txt', 'r')
    line = file.readline()
    user_data = {}
    while line != "":
        tokens = line.split("|")
        username = tokens[0]
        password = tokens[1]
        user_data[username] = password
        line = file.readline()
    file.close()
    return user_data

if __name__ == '__main__':
    run()
