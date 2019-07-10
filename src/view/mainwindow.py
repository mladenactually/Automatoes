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
        lab.setPixmap(QPixmap('tlocrt.png'))
        lab.setFixedSize(640, 320)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(lab)

        #####################################################
        #   Пример додавања дугмића на произвољно место     #
        #####################################################

        fridge = QPushButton('Fridge', lab)
        air_condition = QPushButton('AC', lab)
        fridge.move(10, 10)
        fridge.setFixedSize(20, 20)
        air_condition.move(50, 50)
        air_condition.setFixedSize(20, 20)
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
