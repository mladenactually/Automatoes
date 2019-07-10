from sys import argv, exit

from PyQt5.QtWidgets import QApplication

from src.view.mainwindow import MainWindow


def run():
    app = QApplication(argv)
    window = MainWindow(app)
    window.show()
    exit(app.exec_())


if __name__ == '__main__':
    run()
