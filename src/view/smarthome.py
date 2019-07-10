from src.model.smarthome import SmartHome

from PyQt5.QtWidgets import QWidget


class SmartHomeView(QWidget):
    def __init__(self, home):
        super().__init__()
        self.home = home
