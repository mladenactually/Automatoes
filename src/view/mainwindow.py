from PyQt5.QtWidgets import QWidget, QMainWindow, QStatusBar, QGridLayout, QLabel, QComboBox, QPushButton, QHBoxLayout
from PyQt5.QtGui import QPixmap, QIcon
from PyQt5.QtCore import Qt

from src.view.smarthome import SmartHomeView


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
        home = SmartHomeView(self.app.home)
        self.setCentralWidget(home)
