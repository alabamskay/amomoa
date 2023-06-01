from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from random import *

class Que():
    def __init__(self, quest, r_ans, wrn1, wrn2, wrn3):
        self.quest = quest
        self.r_ans = r_ans
        self.wrn1 = wrn1
        self.wrn2 = wrn2
        self.wrn3 = wrn3


p = QApplication([])
w = QWidget()
w.setGeometry(100,100,400,400)
w.setWindowTitle('Memory card')
Bok = QPushButton('Ответить')
l_q = QLabel('Какой правильный ответ?')

rgb = QGroupBox('Варианты ответов')

rbt1 = QRadioButton('где?')
rbt2 = QRadioButton('кто?')
rbt3 = QRadioButton('когда?')
rbt4 = QRadioButton('почему?')

a1 = QVBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()

a2.addWidget(rbt1)
a2.addWidget(rbt2)
a3.addWidget(rbt3)
a3.addWidget(rbt4)
a1.addLayout(a2)
a1.addLayout(a3)

rgb.setLayout(a1)

l_c = QVBoxLayout()
l_l1 = QHBoxLayout()
l_l2 = QHBoxLayout()
l_l3 = QHBoxLayout()

l_l1.addWidget(l_q, alignment=Qt.AlignCenter)
l_l2.addWidget(rgb)
l_l3.addWidget(Bok, alignment=Qt.AlignCenter)

l_c.addLayout(l_l1, stretch=2)
l_c.addLayout(l_l2, stretch=8)
l_c.addLayout(l_l3, stretch=3)
l_c.setSpacing(5)

w.setLayout(l_c)

AGrB = QGroupBox('Результат теста')

l_res = QLabel('прав ты или нет?')
l_cor = QLabel('Правильный ответ')

lay_res = QVBoxLayout()
lay_res.addWidget(l_res, alignment=(Qt.AlignLeft | Qt.AlignTop))
lay_res.addWidget(l_cor, 2, Qt.AlignCenter)
AGrB.setLayout(lay_res)
l_l2.addWidget(AGrB)

AGrB.hide()
RadGr = QButtonGroup()
RadGr.addButton(rbt1)
RadGr.addButton(rbt2)
RadGr.addButton(rbt3)
RadGr.addButton(rbt4)

def s_tx():
    rgb.show()
    AGrB.hide()
    Bok.setText('Ответить')
    RadGr.setExclusive(False)
    rbt1.setChecked(False)
    rbt2.setChecked(False)
    rbt3.setChecked(False)
    rbt4.setChecked(False)
    RadGr.setExclusive(True)

ans = [rbt1, rbt2, rbt3, rbt4]

def ssres():
    rgb.hide()
    AGrB.show()
    Bok.setText('Следующий вопрос')

def ask(q: Que):
    shuffle(ans)
    ans[0].setText(q.r_ans)
    ans[1].setText(q.wrn1)
    ans[2].setText(q.wrn2)
    ans[3].setText(q.wrn3)
    l_q.setText(q.quest)
    l_cor.setText(q.r_ans)
    s_tx()

def ch_ans():
    if ans[0].isChecked():
        l_res.setText('Правильно!')
        w.score += 1
        print('Статистика\n-Всего вопросов:',w.total,'\n-Правильных ответов:',w.score)
        print('Рейтинг:', (w.score/w.total*100),'%')
    if ans[1].isChecked() or ans[2].isChecked() or ans[3].isChecked():
        l_res.setText('Неверно!')
        print('Рейтинг:', (w.score/w.total*100),'%')
    ssres()
w.c_q = -1

ql = []
ql.append(Que('Сколько спутников у Марса','2','13','50','1'))
ql.append(Que('В какой из следующих империй не было письменности:','инков','ацтеков','египтян','римлян'))
ql.append(Que('Какой планеты не существует?','Венеций','Плутон','Авасис','Друкюль'))
ql.append(Que('Какая кошка самая большая на планете?','тигр','лев','гепард','барс'))
ql.append(Que('Символом Рима является скульптурное изображение волчицы, Берлина- изображение медведя. А что является символом Копенгагена?','Русалочка','лев','лебедь','кот в мешке'))
ql.append(Que('В Англии существует закон, согласно которому за наезд на животное наказание строже, чем за наезд на людей. Считается, что животное беззащитно перед автомобилем, потому что…?','не знал ПДД','не может от него убежать','не разбираетя в автомобилях','слишком глупые'))
ql.append(Que('Какой персонаж самый умный в Цветочном городе?','Мальвина','Степан','Маугли','Дровесек'))
ql.append(Que('Какое животное носила с собой Шапокляк?','Крысу Лориску','Крокодила Гену','Кота Леопольда','Мышь Джерри'))
ql.append(Que('Что любят кушать панды?','бамбук','сало','пиццу','ландыш'))
ql.append(Que('Арбуз - это фрукт или ягода?','ягода','фрукт','овощ','переодная стадия'))

def nextq():
    w.total += 1
    print('Статистика\n-Всего вопросов:',w.total,'\n-Правильных ответов:',w.score)
    c_q2 = randint(0,len(ql) - 1)
    q = ql[c_q2]
    ask(q)

def click_ok():
    if Bok.text() == 'Ответить':
        ch_ans()
    else:
        nextq()

c_q2 = -1
w.score = 0
w.total = 0

Bok.clicked.connect(click_ok)
nextq()
w.show()
p.exec_()