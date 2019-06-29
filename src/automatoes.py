from sys import argv, exit

from PyQt5.QtWidgets import QApplication, QWidget

def run():
    app = QApplication(argv)

    widget = QWidget()
    widget.resize(640, 480)
    widget.move(400, 400)
    widget.setWindowTitle('Automatoes')
    widget.show()

    exit(app.exec_())

if __name__ == '__main__':
    run()
