import sys

from PyQt5.QtGui import QImage, QPixmap, QColor, QTransform
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QButtonGroup, QFileDialog, QLabel


class MyPillow(QWidget):
    def __init__(self):
        super().__init__()
        self.resize(576, 500)
        self.setWindowTitle('PIL 2.0')

        self.channelButtons = QButtonGroup(self)
        self.rotateButtons = QButtonGroup(self)

        self.pushButton3 = QPushButton('ALL', self)
        self.pushButton3.setGeometry(56, 260, 75, 23)
        self.channelButtons.addButton(self.pushButton3)

        self.pushButton = QPushButton('R', self)
        self.pushButton.setGeometry(56, 50, 75, 23)
        self.channelButtons.addButton(self.pushButton)

        self.pushButton1 = QPushButton('G', self)
        self.pushButton1.setGeometry(56, 120, 75, 23)
        self.channelButtons.addButton(self.pushButton1)

        self.pushButton2 = QPushButton('B', self)
        self.pushButton2.setGeometry(56, 190, 75, 23)
        self.channelButtons.addButton(self.pushButton2)

        self.pushButton_4 = QPushButton('Против часовой стрелки', self)
        self.pushButton_4.setGeometry(20, 360, 271, 41)
        self.rotateButtons.addButton(self.pushButton_4)
        self.pushButton_4.clicked.connect(self.R)

        self.pushButton5 = QPushButton('По часовой стрелке', self)
        self.pushButton5.setGeometry(300, 360, 261, 41)
        self.rotateButtons.addButton(self.pushButton5)
        self.pushButton5.clicked.connect(self.L)

        self.image = QLabel(self)
        self.image.move(200, 40)
        self.image.resize(300, 300)

        self.fname = QFileDialog.getOpenFileName(self, 'Выбрать картинку', '')[0]
        self.zxc = QImage(self.fname)
        self.curr_image = self.zxc.copy()
        self.pix = QPixmap.fromImage(self.curr_image).scaled(300, 300)
        self.image.setPixmap(self.pix)
        for i in self.channelButtons.buttons():
            i.clicked.connect(self.qwe)

    def qwe(self):
        W, H = self.curr_image.width(), self.curr_image.height()
        for x in range(W):
            for y in range(H):
                R, G, B, _ = self.zxc.pixelColor(x, y).getRgb()
                if self.sender().text() == 'R':
                    self.curr_image.setPixelColor(x, y, QColor(R, 0, 0))
                if self.sender().text() == 'G':
                    self.curr_image.setPixelColor(x, y, QColor(0, G, 0))
                if self.sender().text() == 'B':
                    self.curr_image.setPixelColor(x, y, QColor(0, 0, B))
                if self.sender().text() == 'ALL':
                    self.curr_image.setPixelColor(x, y, QColor(R, G, B))

        self.pix = QPixmap.fromImage(self.curr_image).scaled(300, 300)
        self.image.setPixmap(self.pix)

    def R(self):
        s = QTransform().rotate(-90)
        self.zxc = self.zxc.transformed(s)
        self.curr_image = self.curr_image.transformed(s)
        self.pix = QPixmap.fromImage(self.curr_image).scaled(300, 300)
        self.image.setPixmap(self.pix)

    def L(self):
        s = QTransform().rotate(90)
        self.zxc = self.zxc.transformed(s)
        self.curr_image = self.curr_image.transformed(s)
        self.pix = QPixmap.fromImage(self.curr_image).scaled(300, 300)
        self.image.setPixmap(self.pix)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyPillow()
    ex.show()
    sys.exit(app.exec_())
