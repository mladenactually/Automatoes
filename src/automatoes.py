from sys import argv, exit

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar, QGridLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt
class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setWindowTitle("Automatoes")
        self.setWindowIcon(QIcon('automato.png'))
        desktop = app.desktop()
        height = desktop.screenGeometry().height()
        width = desktop.screenGeometry().width()
        self.setGeometry(width/4 - 100, height/4 - 100, width/2, height/2)
        self.setFixedSize(width/2 + 200, height/2 + 200)

    def setupComponents(self):
        self.statusBarSetup()
        self.centralWidgetSetup()


    def statusBarSetup(self):
        myStatusBar = QStatusBar()
        self.setStatusBar(myStatusBar)
        label1 = QLabel()
        label1.setText("Label 1")
        label1.show()
        myStatusBar.addWidget(label1, 1)

    def centralWidgetSetup(self):
        cent_widg = QWidget()

        layout = QGridLayout()

        lab = QLabel()
        lab.setPixmap(QPixmap('tlocrt.png'))
        lab.setFixedSize(640, 320)
        layout.setAlignment(Qt.AlignCenter)
        layout.addWidget(lab)

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






def run():
    app = QApplication(argv)
    window = MainWindow(app)
    window.setupComponents()
    window.show()
    exit(app.exec_())

if __name__ == '__main__':
    run()
