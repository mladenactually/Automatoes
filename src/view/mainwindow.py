from PyQt5.QtWidgets import QWidget, QMainWindow, QStatusBar, QGridLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt


class MainWindow(QMainWindow):
    def __init__(self, app):
        super().__init__()
        self.app = app
        self.setWindowTitle("Automatoes")
        self.setWindowIcon(QIcon('automato.png'))
        desktop = app.desktop()
        height = desktop.screenGeometry().height()
        width = desktop.screenGeometry().width()
        self.setGeometry(width/4 - 100, height/4 - 100, width/2, height/2)
        self.setFixedSize(width/2 + 200, height/2 + 200)
        self.setup_components()

    def setup_components(self):
        self.statusbar_setup()
        self.central_widget_setup()

    def statusbar_setup(self):
        stat = QStatusBar()
        self.setStatusBar(stat)
        label1 = QLabel()
        label1.setText("Label 1")
        label1.show()
        stat.addWidget(label1, 1)

    def central_widget_setup(self):
        cent_widg = QWidget()

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
        air_condition = QPushButton('AC', lab)
        dish_washer = QPushButton('Dish \n Washer', lab)
        oven = QPushButton('Oven', lab)
        stove = QPushButton('Stove', lab)
        microwave = QPushButton('Microwave', lab)
        washing_machine = QPushButton('Washing \n machine', lab)
        dryer = QPushButton('Dryer', lab)
        tv = QPushButton('Tv', lab)
        stereo = QPushButton('Stereo',lab)
        computer = QPushButton('Computer', lab)
        kitchen_light = QPushButton('Light', lab)
        bathroom_light = QPushButton('Light', lab)
        living_room_light = QPushButton('Light', lab)
        first_room_light = QPushButton('Light', lab)
        second_room_light = QPushButton('Light', lab)


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

        device_menu = QComboBox()
        layout.addWidget(device_menu, 1, 0)
        label = QLabel("Bills")
        layout.addWidget(label, 2, 0)
        water_button = QPushButton("Water Bill")
        gas_button = QPushButton("Gas Bill")
        electricity_button = QPushButton("Elactricity Bill")
        internet_button = QPushButton("Internet Bill")
        button_layout = QHBoxLayout()
        button_layout.addWidget(water_button)
        button_layout.addWidget(gas_button)
        button_layout.addWidget(electricity_button)
        button_layout.addWidget(internet_button)
        bts = QWidget()
        bts.setLayout(button_layout)
        layout.addWidget(bts, 3, 0)
        cent_widg.setLayout(layout)
        self.setCentralWidget(cent_widg)
