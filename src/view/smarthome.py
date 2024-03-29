from src.model.smarthome import SmartHome
from src.view.device_dialog import DeviceDialog
from src.view.bill_dialog import BillDialog
from PyQt5.QtWidgets import QWidget, QMainWindow, QStatusBar, QGridLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class SmartHomeView(QWidget):
    def __init__(self, home):
        super().__init__()
        self.home = home
        self.central_widget_setup()


    def central_widget_setup(self):
        layout = QGridLayout()

        lab = QLabel()
        lab.setPixmap(QPixmap('tlocrt2.png'))
        lab.setFixedSize(640, 320)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(lab)

        #####################################################
        #   Пример додавања дугмића на произвољно место     #
        #####################################################

        fridge = QPushButton('Fridge', lab)
        fridge.clicked.connect(self.open_fridge)
        air_condition = QPushButton('AC', lab)
        air_condition.clicked.connect(self.open_ac)
        dish_washer = QPushButton('Dish \n Washer', lab)
        dish_washer.clicked.connect(self.open_dishw)
        oven = QPushButton('Oven', lab)
        oven.clicked.connect(self.open_oven)
        stove = QPushButton('Stove', lab)
        stove.clicked.connect(self.open_stove)
        microwave = QPushButton('Microwave', lab)
        microwave.clicked.connect(self.open_micro)
        washing_machine = QPushButton('Washing \n machine', lab)
        washing_machine.clicked.connect(self.open_washma)
        dryer = QPushButton('Dryer', lab)
        dryer.clicked.connect(self.open_dryer)
        tv = QPushButton('Tv', lab)
        tv.clicked.connect(self.open_tv)
        stereo = QPushButton('Stereo', lab)
        stereo.clicked.connect(self.open_stereo)
        computer = QPushButton('Computer', lab)
        computer.clicked.connect(self.open_comp)
        kitchen_light = QPushButton('Light', lab)
        kitchen_light.clicked.connect(self.open_kitchenl)
        bathroom_light = QPushButton('Light', lab)
        bathroom_light.clicked.connect(self.open_bathrooml)
        living_room_light = QPushButton('Light', lab)
        living_room_light.clicked.connect(self.open_livingl)
        first_room_light = QPushButton('Light', lab)
        first_room_light.clicked.connect(self.open_leftrooml)
        second_room_light = QPushButton('Light', lab)
        second_room_light.clicked.connect(self.open_rightrooml)


        #KITCHEN

        #fridge
        fridge.move(260, 30)
        fridge.setFixedSize(40, 40)
        #dish_washer
        dish_washer.move(190,30)
        dish_washer.setFixedSize(70,40)
        #oven
        oven.move(150, 30)
        oven.setFixedSize(40, 40)
        #stove
        stove.move(150, 70)
        stove.setFixedSize(40, 40)
        #microwave
        microwave.move(150, 110)
        microwave.setFixedSize(70, 40)
        #light
        kitchen_light.move(210, 160)
        kitchen_light.setFixedSize(40, 30)

        #BATHROOM
        #washin_machine
        washing_machine.move(10, 30)
        washing_machine.setFixedSize(70, 40)
        #dryer
        dryer.move(80, 30)
        dryer.setFixedSize(60, 40)
        #light
        bathroom_light.move(60, 100)
        bathroom_light.setFixedSize(40, 30)


        #LIVING ROOM

        tv.move(10, 220)
        tv.setFixedSize(20, 50)

        stereo.move(95,195)
        stereo.setFixedSize(50, 30)

        # air_condition
        air_condition.move(270, 240)
        air_condition.setFixedSize(30, 50)

        living_room_light.move(60, 230)
        living_room_light.setFixedSize(40, 30)

        #ROOMS

        computer.move(455, 260)
        computer.setFixedSize(57, 30)

        first_room_light.move(340, 160)
        first_room_light.setFixedSize(40, 30)

        second_room_light.move(450, 160)
        second_room_light.setFixedSize(40, 30)




        # дакле, када правимо QPushButton дугме, ставимо да му је родитељ
        # lab (тј. слика тлоцрта) тако што ту лабелу проследимо као други аргумент
        # онда можемо ручно да му подесимо димензије (setFixedSize) и позицију (move)

        #Dropdown menu
        self.device_menu = QComboBox()
        layout.addWidget(self.device_menu, 1, 0)
        self.device_menu.addItem('')
        self.device_menu.addItem('KITCHEN')
        self.device_menu.addItem('       Fridge')
        self.device_menu.addItem('       Dish washer')
        self.device_menu.addItem('       Stove')
        self.device_menu.addItem('       Oven')
        self.device_menu.addItem('       Microwave')
        self.device_menu.addItem('       Kitchen light')
        self.device_menu.addItem('LIVING ROOM')
        self.device_menu.addItem('       Tv')
        self.device_menu.addItem('       AC')
        self.device_menu.addItem('       Stereo')
        self.device_menu.addItem('       Livingroom light')
        self.device_menu.addItem('BATHROOM')
        self.device_menu.addItem('       Washing machine')
        self.device_menu.addItem('       Dryer')
        self.device_menu.addItem('       Bathroom light')
        self.device_menu.addItem('ROOMS')
        self.device_menu.addItem('       Left room light')
        self.device_menu.addItem('       Right room light')
        self.device_menu.addItem('       Computer')
        self.device_menu.activated.connect(self.open_box)
        label = QLabel("Bills")
        layout.addWidget(label, 2, 0)
        water_button = QPushButton("Water Bill")
        water_button.clicked.connect(self.open_water_bill)
        gas_button = QPushButton("Gas Bill")
        gas_button.clicked.connect(self.open_gas_bill)
        electricity_button = QPushButton("Electricity Bill")
        electricity_button.clicked.connect(self.open_electricty_bill)
        internet_button = QPushButton("Internet Bill")
        internet_button.clicked.connect(self.open_internet_bill)
        button_layout = QHBoxLayout()
        button_layout.addWidget(water_button)
        button_layout.addWidget(gas_button)
        button_layout.addWidget(electricity_button)
        button_layout.addWidget(internet_button)
        bts = QWidget()
        bts.setLayout(button_layout)
        layout.addWidget(bts, 3, 0)
        self.setLayout(layout)

    def open_dialog(self, name):
        device = self.home.devices[name]
        dialog = DeviceDialog(device)
        dialog.show()
        dialog.exec_()

    def open_box(self):
        invalid = ['KITCHEN', 'BATHROOM', 'ROOMS', 'LIVING ROOM', '']
        if not self.device_menu.currentText() in invalid:
            self.open_dialog(self.device_menu.currentText()[7:])

    def open_fridge(self):
        self.open_dialog('Fridge')

    def open_stove(self):
        self.open_dialog('Stove')

    def open_dishw(self):
        self.open_dialog('Dish washer')

    def open_oven(self):
        self.open_dialog('Oven')

    def open_micro(self):
        self.open_dialog('Microwave')

    def open_kitchenl(self):
        self.open_dialog('Kitchen light')

    def open_washma(self):
        self.open_dialog('Washing machine')

    def open_dryer(self):
        self.open_dialog('Dryer')

    def open_bathrooml(self):
        self.open_dialog('Bathroom light')

    def open_tv(self):
        self.open_dialog('Tv')

    def open_ac(self):
        self.open_dialog('AC')

    def open_livingl(self):
        self.open_dialog('Livingroom light')

    def open_stereo(self):
        self.open_dialog('Stereo')

    def open_leftrooml(self):
        self.open_dialog('Left room light')

    def open_rightrooml(self):
        self.open_dialog('Right room light')

    def open_comp(self):
        self.open_dialog('Computer')

    def open_bill_dialog(self, unit, home):
        dialog = BillDialog(unit, home)
        dialog.show()
        dialog.exec_()

    def open_water_bill(self):
        self.open_bill_dialog('Water', self.home)

    def open_gas_bill(self):
        self.open_bill_dialog('Gas', self.home)

    def open_electricty_bill(self):
        self.open_bill_dialog('Electricity', self.home)

    def open_internet_bill(self):
        self.open_bill_dialog('Internet', self.home)