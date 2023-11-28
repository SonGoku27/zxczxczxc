from PyQt5 import QtCore, QtWidgets
from PyQt5.QtGui import QPolygon
from sys import argv, exit
from PyQt5.QtCore import Qt, QPoint
from PyQt5.QtGui import QPainter, QColor
from random import choice, randint
from PyQt5.QtWidgets import QApplication, QMainWindow


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.resize(500, 500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 0, 500, 500))
        MainWindow.setCentralWidget(self.centralwidget)
        MainWindow.setWindowTitle("Супрематизм")


class Main(Ui_MainWindow, QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.x = -1
        self.y = -1
        self.k = 0
        self.colors = ['Red', 'Orange', 'Yellow', 'Green', 'Cyan',
                       'Blue', 'Magenta', 'Purple', 'Brown', 'Black']

    def mousePressEvent(self, event):
        self.x = event.x()
        self.y = event.y()
        if event.button() == Qt.LeftButton:
            self.k = 1
        elif event.button() == Qt.RightButton:
            self.k = -1
        self.update()

    def keyPressEvent(self, event):
        if event.key() == Qt.Key_Space:
            self.k = 2
            self.update()

    def mouseMoveEvent(self, event):
        self.setMouseTracking(True)
        self.x_coor = event.x()
        self.y_coor = event.y()
        print(self.x_coor, self.y_coor)

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.drawing(qp)
        qp.end()

    def drawing(self, qp):
        if self.x > -1 and self.y > -1 and self.k == 1:
            qp.setBrush(QColor(choice(self.colors)))
            qp.drawRect(self.x, self.y, randint(1, 100), randint(1, 100))
            ex.show()

        elif self.x > -1 and self.y > -1 and self.k == -1:
            qp.setBrush(QColor(choice(self.colors)))
            a = randint(1, 100)
            qp.drawEllipse(self.x, self.y, a, a)

        elif self.x > -1 and self.y > -1 and self.k == 2:
            qp.setBrush(QColor(choice(self.colors)))
            width = randint(20, 100)
            points = QPolygon([QPoint(self.x, self.y), QPoint(self.x + width,
                                                              self.y + width),
                               QPoint(self.x - width,
                                      self.y + width)])
            qp.drawPolygon(points)


if __name__ == '__main__':
    app = QApplication(argv)
    ex = Main()
    ex.show()
    exit(app.exec())
