from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget,QTableWidget,  QListView, QListWidgetItem, QFormLayout, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QLabel, QPushButton, QSpinBox
app =QApplication([])
#віджети
menu_btn = QPushButton("Меню")
sleep_btn = QPushButton('Відпочити')
time_sleep = QSpinBox()
time_sleep.setValue(30)
okyn_btn = QPushButton('Відповісти')
okyn_lb = QLabel('###')

#панель з відповідями
RadioGroupBox = QGroupBox('варіанти відповідей')
RadioGroup = QButtonGroup()
rdbt_1 = QRadioButton('###')
rdbt_2 = QRadioButton('###')
rdbt_3 = QRadioButton('###')
rdbt_4 = QRadioButton('###')
RadioGroup.addButton(rdbt_1)
RadioGroup.addButton(rdbt_2)
RadioGroup.addButton(rdbt_3)
RadioGroup.addButton(rdbt_4)

#панель з результатами
resultGroupBox = QGroupBox('Результат тесту')
result_lb = QLabel('#')
result_true_lb = QLabel('#')

#розміщення 
layout_an1 = QHBoxLayout()
layout_an2 = QVBoxLayout()
layout_an3 = QVBoxLayout()

layout_an2.addWidget(rdbt_1)
layout_an2.addWidget(rdbt_2)

layout_an3.addWidget(rdbt_3)
layout_an3.addWidget(rdbt_4)

layout_an1.addLayout(layout_an2)
layout_an1.addLayout(layout_an3)
RadioGroupBox.setLayout(layout_an3)
#розміщення результату
layout_res = QVBoxLayout()
layout_res.addWidget(result_lb, alignment=Qt.AlignLeft|Qt.AlignTop)
layout_res.addWidget(result_true_lb, alignment=Qt.AlignHCenter, stretch = 2 )
resultGroupBox.setLayout(layout_res)
resultGroupBox.hide()

#розміщення віджетів
layout_line1  = QHBoxLayout()
layout_line2  = QHBoxLayout()
layout_line3  = QHBoxLayout()
layout_line4  = QHBoxLayout()

layout_line1.addWidget(menu_btn)
layout_line1.addStretch(1)
layout_line1.addWidget(sleep_btn)
layout_line1.addWidget(time_sleep)

layout_line2.addWidget(okyn_lb)

layout_line3.addWidget(RadioGroupBox)
layout_line3.addWidget(result_lb)

layout_line4.addStretch(1)
layout_line4.addWidget(okyn_btn, stretch = 2)
layout_line4.addStretch(1)

card_layout = QVBoxLayout()
card_layout.addLayout(layout_line1, stretch=1)
card_layout.addLayout(layout_line2, stretch=2)
card_layout.addLayout(layout_line3, stretch=8)
card_layout.addStretch(1)
card_layout.addLayout(layout_line4, stretch=1)
card_layout.addStretch(1)
card_layout.setSpacing(5)

#result
def show_result():
    RadioGroupBox.hide()
    resultGroupBox.show()
    okyn_btn.setText("Наступне")

def show_question():
    RadioGroupBox.show()
    resultGroupBox.hide()
    okyn_btn.setText("відповісти")

RadioGroup.setExclusive(False)
rdbt_1.setChecked(False)
rdbt_2.setChecked(False)
rdbt_3.setChecked(False)
rdbt_4.setChecked(False)
RadioGroup.setExclusive(True)



