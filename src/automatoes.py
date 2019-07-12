from sys import argv, exit
import os
from src.view.device_dialog import DeviceL
from src.model.smarthome import SmartHome
from PyQt5.QtWidgets import QApplication, QDialog, QHBoxLayout, QLabel
from src.view.login_dialog import LoginDialog
from src.view.mainwindow import MainWindow


def run():
    user_data = load_user_data()
    for item in user_data.keys():
        print(item, user_data[item])
    app = QApplication(argv)
    dialog = LoginDialog()
    dialog.show()
    dialog.exec_()
    while not login(user_data, dialog.username, dialog.password):
        if dialog.exit:
            break
        dialog.wrong()
        dialog.show()
        dialog.exec_()
    if login(user_data, dialog.username, dialog.password):
        open_main_window(app)
    exit(0)


def open_main_window(app):
    app.home = home_setup()

    window = MainWindow(app)
    window.show()
    exit(app.exec_())


def devices_setup():
    devices = {}
    # kitchen
    fr = DeviceL('fridge', 100, 0, 0)
    devices['Fridge'] = fr
    st = DeviceL('Stove', 80, 0, 50)
    devices['Stove'] = st
    dw = DeviceL('Dish washer', 120, 60, 0)
    devices['Dish washer'] = dw
    ov = DeviceL('Oven', 100, 0, 0)
    devices['Oven'] = ov
    mw = DeviceL('Microwave', 30, 0, 0)
    devices['Microwave'] = mw
    kl = DeviceL('Kitchen light', 25, 0, 0)
    devices["Kitchen light"] = kl

    # bathroom

    wm = DeviceL('Washing machine', 120, 50, 0)
    devices['Washing machine'] = wm
    dr = DeviceL('Dryer', 100, 0, 0)
    devices['Dryer'] = dr
    bl = DeviceL('Bathroom light', 25, 0, 0)
    devices['Bathroom light'] = bl

    # livingroom

    tv = DeviceL('tv', 100, 0, 0)
    devices['Tv'] = tv
    ac = DeviceL('Air condition', 100, 0, 0)
    devices['AC'] = ac
    ll = DeviceL('Livingroom light', 25, 0, 0)
    devices['Livingroom light'] = ll
    se = DeviceL('Stereo', 40, 0, 0)
    devices['Stereo'] = se

    # rooms

    lrl = DeviceL('Left room light', 25, 0, 0)
    devices['Left room light'] = lrl
    rrl = DeviceL('Right room light', 25, 0, 0)
    devices['Right room light'] = rrl
    cp = DeviceL('Computer', 70, 0, 0)
    devices['Computer'] = cp

    return devices

def home_setup():
    devices = devices_setup()
    home = SmartHome(None, devices, 5000)
    return home


def login(user_data, username, password):
    if username in user_data:
        if user_data[username][3] == password:
            return True
        else:
            return False
    else:
        return False

def logout():
    pass

def load_user_data():
    file = open(".." + os.sep + "Data" + os.sep + 'user_data.txt', 'r')
    line = file.readline()
    user_data = {}
    while line != "":
        tokens = line.strip().split("|")
        name = tokens[0]
        last_name = tokens[1]
        username = tokens[2]
        password = tokens[3]
        data = [name, last_name, username, password]
        user_data[username] = data
        line = file.readline()
    file.close()
    return user_data


if __name__ == '__main__':
    run()
