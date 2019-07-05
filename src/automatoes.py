from sys import argv, exit

from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow, QStatusBar, QGridLayout, QLabel, QHBoxLayout, QTextEdit
from PyQt5.QtGui import QPixmap
class MainWindow(QMainWindow):
    def __init__(self, app):
        super(MainWindow, self).__init__()
        self.app = app
        self.setWindowTitle("Automatoes")
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
        widget_layout = QHBoxLayout()
        cent_widg = QWidget()
        cent_widg.setLayout(widget_layout)
        left_layout = QGridLayout()

        lab = QLabel()
        lab.setPixmap(QPixmap('tlocrt.png'))
        left_layout.addWidget(lab,0,0)
        left = QWidget()
        left.setLayout(left_layout)

        right = QTextEdit()
        widget_layout.addWidget(left)
        widget_layout.addWidget(right)
        self.setCentralWidget(cent_widg)






def run():
    app = QApplication(argv)
    window = MainWindow(app)
    window.setupComponents()
    window.show()
    exit(app.exec_())

if __name__ == '__main__':
    run()
