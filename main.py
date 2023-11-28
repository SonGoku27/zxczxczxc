import sqlite3
import sys

from PyQt5.QtGui import QPainter, QColor, QPixmap, QIcon, QFont
from PyQt5.QtWidgets import QWidget, QLineEdit, QApplication, QPushButton, QLabel, QMessageBox, QComboBox
from PyQt5.QtCore import QSize


# Я пишу очень плохой код ;((((
class FiveLetters(QWidget):
    def __init__(self):
        super().__init__()

        self.curr_row = 0
        self.num = 5
        self.spis = []
        self.do_paint = False
        self.word = ''
        con = sqlite3.connect('words.sqlite')
        cur = con.cursor()
        sqw = cur.execute("""SELECT win FROM save WHERE id = 1""").fetchall()
        self.win1 = sqw[0][0]
        con.close()

        self.dsl = QMessageBox()
        self.dsl.setWindowTitle('Дисклеймер')
        self.dsl.setText('Игра только для честных людей')
        self.dsl.exec_()

        self.resize(600, 600)
        self.setWindowTitle('Игра бога')

        self.pixmap1 = QPixmap("DSA.png").scaled(600, 400)
        self.image1 = QLabel(self)
        self.image1.move(0, 0)
        self.image1.resize(600, 400)
        self.image1.setPixmap(self.pixmap1)
        self.image1.show()

        self.pixmap2 = QPixmap("zxcd.jpg").scaled(600, 600)
        self.image2 = QLabel(self)
        self.image2.move(0, 0)
        self.image2.resize(600, 600)
        self.image2.setPixmap(self.pixmap2)

        self.start = QPushButton(self)
        self.start.resize(120, 120)
        self.start.move(234, 222)
        self.start.setIcon(QIcon('zxcd2.jpg'))
        self.start.setIconSize(QSize(140, 120))
        self.start.clicked.connect(self.zxc2)

        self.button = QPushButton('ПОТВЕРДИТЬ', self)
        self.button.setStyleSheet('background: rgb(255, 215, 0);font-size: 30px;')
        self.button.resize(300, 55)
        self.button.move(100, 450)
        self.button.clicked.connect(self.zxc)
        self.button.hide()

        self.lable0 = QLabel(self)
        self.lable0.resize(100, 100)
        self.lable0.move(400, 192)
        self.lable0.setText('Удачи!')
        self.lable0.show()

        self.lable1 = QLabel(self)
        self.lable1.move(10, 50)
        self.lable1.resize(600, 400)
        self.lable1.setText('')
        self.lable1.hide()

        self.lable2 = QLabel(self)

    # Как же я плох в программировании ;(((
    def Data_Base(self):
        con = sqlite3.connect('words.sqlite')
        cur = con.cursor()
        result = list(set(cur.execute(
            f"""SELECT word from WORDS where letters_id = (SELECT id from wordnum 
                    where letters = {self.num})""").fetchall()))
        self.word = result[0][0].lower()
        con.close()

    def answer_forms(self):
        y = 20
        for i in range(self.num):
            x = 10
            row = []
            for j in range(self.num):
                QLD = QLineEdit(self)
                QLD.resize(80, 80)
                QLD.move(x, y)
                QLD.hide()
                QLD.setMaxLength(1)
                QLD.setStyleSheet('background: rgb(192, 192, 192);font-size: 70px;')
                row.append(QLD)
                x += 80
            y += 80
            self.spis.append(row)

    def zxc2(self):
        self.start.hide()
        self.image2.hide()
        self.paint()

        self.button2 = QPushButton('Потвердить', self)
        self.button2.resize(120, 40)
        self.button2.move(340, 250)
        self.button2.clicked.connect(self.gul)
        self.button2.setStyleSheet('background: rgb(255, 215, 0);font-size: 20px;')
        self.button2.show()

        self.combo = QComboBox(self)
        self.combo.resize(120, 40)
        self.combo.move(200, 250)
        self.combo.addItems(["5 букв", "6 букв"])
        self.combo.activated[str].connect(self.onActivated)
        self.combo.show()

    def onActivated(self, text):
        self.num = int(text[0])
        print(self.num)

    def gul(self):
        self.lable3 = QLabel(self)
        self.lable3.move(410, 470)
        self.lable3.setText('Побед: ' + str(self.win1))
        self.lable3.resize(100, 30)
        self.lable3.show()
        self.answer_forms()
        self.Data_Base()
        self.button.show()
        self.button2.hide()
        self.combo.hide()
        for i in self.spis[0]:
            i.show()

    # В чём смысл моей жизни ?????????????
    def zxc(self):
        w = ''
        x = 0

        for i in self.spis[self.curr_row]:
            if i.text().lower() not in 'ёйцукенгшщзхъфывапролджэячсмитьбю' or i.text() == '':
                return

        for i in self.spis[self.curr_row]:
            w += i.text()

            if i.text() in self.word:
                i.setStyleSheet('background: rgb(255, 255, 0);'
                                'font-size: 70px;'
                                'color: rgb(0, 0, 0);')

            if i.text() == self.word[x]:
                i.setStyleSheet('background: rgb(60, 170, 60);'
                                'font-size: 70px;'
                                'color: rgb(255, 255, 255);')

            x += 1
            i.setEnabled(False)

        if w == self.word:
            self.win()
        elif w != self.word and self.curr_row == 4:
            self.lose()
        else:
            for i in self.spis[min(self.curr_row + 1, self.num - 1)]:
                i.show()
            self.curr_row += 1

    def win(self):
        for i in self.spis:
            for j in i:
                j.hide()
        self.lable1.setStyleSheet("font-size: 70px")
        self.lable1.setText('ВЫ ПОБЕДИЛИ!')
        font2 = QFont()
        font2.setFamily('Comic Sans MS')
        font2.setBold(True)
        self.lable1.setFont(font2)
        self.lable2.setStyleSheet("font-size: 45px;color: rgb(255, 0, 0)")
        self.lable0.setStyleSheet("font-size: 11px")
        self.lable0.setText('МОЛОДЕЦ!')
        con = sqlite3.connect('words.sqlite')
        cur = con.cursor()
        cur.execute('UPDATE save SET win = ? where id = 1', (self.win1 + 1,))
        con.commit()
        self.hiding()

    def lose(self):
        for i in self.spis:
            for j in i:
                j.hide()
        self.lable1.setStyleSheet("font-size: 70px")
        self.lable1.setText('ВЫ ПРОИГРАЛИ')
        font2 = QFont()
        font2.setFamily('Comic Sans MS')
        font2.setBold(True)
        self.lable1.setFont(font2)

        self.lable2.setStyleSheet("font-size: 45px;color: rgb(0, 0, 255)")
        self.lable0.setStyleSheet("font-size: 20px")
        self.lable0.setText('ой!')
        self.hiding()

    def paint(self):
        self.do_paint = True
        self.update()

    def paint2(self):
        self.do_paint = False
        self.update()

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        self.draw_flag(qp)
        qp.end()

    def draw_flag(self, qp):
        if self.do_paint:
            qp.setBrush(QColor(139, 69, 19))
            qp.drawRect(0, 400, 600, 600)
            qp.setBrush(QColor(60, 170, 60))
            qp.drawRect(30, 520, 30, 30)
            qp.setBrush(QColor(255, 255, 0))
            qp.drawRect(30, 560, 30, 30)

            self.lab1 = QLabel(self)
            self.lab1.move(70, 525)
            self.lab1.setText('Буква находится в слове, на своём месте')

            self.lab2 = QLabel(self)
            self.lab2.move(70, 565)
            self.lab2.setText('Буква находится в слове')

            self.lab1.show()
            self.lab2.show()
        self.do_paint = False

    def hiding(self):
        self.paint()
        self.lab2.hide()
        self.lab1.hide()
        self.lable0.show()
        self.lable1.show()
        self.lable1.move(10, 50)
        self.lable1.resize(600, 400)
        self.lable1.setStyleSheet("font-size: 70px")
        self.lable2.move(30, 120)
        self.lable2.resize(600, 400)
        self.lable2.show()
        self.button.hide()
        self.lable2.setText('Ваше слово было: ' + self.word.capitalize())


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FiveLetters()
    ex.show()
    sys.exit(app.exec())
