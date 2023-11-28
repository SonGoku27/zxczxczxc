import sys
import random

from PyQt5.QtGui import QPainter, QColor, QPolygonF
from PyQt5.QtCore import Qt, QPointF, QPoint
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Suprematism(QWidget):
    def __init__(self):
        super().__init__()
        self.x = -1
        self.y = -1
        self.do_paint = 0
        self.initUI()

    def initUI(self):
        self.resize(1000, 1000)
        self.setWindowTitle('Suprematism')

        self.coords = QLabel(self)
        self.coords.setText("Координаты: None, None")
        self.coords.move(30, 30)

    def mouseMoveEvent(self, event):
        self.setMouseTracking(True)
        self.x = event.x()
        self.y = event.y()
        self.coords.setText(f"Координаты: {event.x()}, {event.y()}")

    def mousePressEvent(self, event):
        self.delet()
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.do_paint = 1
        elif event.button() == Qt.RightButton:
            self.do_paint = 2
        self.update()

    def keyPressEvent(self, event):
        self.delet()
        if event.key() == Qt.Key_Space:
            self.do_paint = 3
            print('пробел')
            self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        self.zxc = random.randint(20, 100)
        qp.setBrush(QColor(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))
        if self.x > -1 and self.y > -1 and self.do_paint == 1:
            self.draw_ellips(qp)
            print('r')
        elif self.x > -1 and self.y > -1 and self.do_paint == 2:
            self.draw_reck(qp)
            print('e')
        elif self.x > -1 and self.y > -1 and self.do_paint == 3:
            self.draw_polig(qp)
            print('p')

    def draw_reck(self, qp):
        qp.drawRect(QRectF(self.x - self.zxc // 2, self.y - self.zxc // 2, self.zxc, self.zxc))

    def draw_polig(self, qp):
        points = QPolygonF(
            [QPointF(float(self.x + 0 * self.zxc), float(self.y + -1 * self.zxc)),
             QPointF(float(self.x + -0.86602540378443864676372317075294 * self.zxc), float(self.y + self.zxc * 0.5)),
             QPointF(float(self.x + self.zxc * 0.86602540378443864676372317075294), float(self.y + self.zxc * 0.5))])
        qp.drawPolygon(points)

    def draw_ellips(self, qp):
        qp.drawEllipse(QPointF(float(self.x), float(self.y)), self.zxc, self.zxc)

    def delet(self):
        self.do_paint = 0
        self.update()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec())
