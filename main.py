import sys
import random

from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton
from PyQt5 import uic


class App(QWidget):
    def __init__(self):
        super(App, self).__init__()
        self.paint = False
        uic.loadUi('untitled.ui', self)
        self.setWindowTitle('Желтые круги')
        self.pushButton.clicked.connect(self.do_paint)

    def paintEvent(self, event):
        if self.paint:
            qp = QPainter()
            qp.begin(self)
            self.drawCircles(qp)
            qp.end()

    def do_paint(self):
        self.paint = True
        self.repaint()

    def drawCircles(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        for i in range(random.randint(1, 10)):
            j = random.randint(20, 100)
            qp.drawEllipse(random.randint(0, 200), random.randint(0, 200), j, j)


def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    sys.excepthook = except_hook
    app = QApplication(sys.argv)
    ex = App()
    ex.show()
    sys.exit(app.exec())

