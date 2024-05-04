from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QFileDialog
from seminar_4.sound_file_converted import Audio_Item

class MyWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setMinimumSize(600,400)

        mainLayout=QHBoxLayout()
        verticalLayout=QVBoxLayout()

        mainLayout.addLayout(verticalLayout)

        self.setLayout(mainLayout)

        self.myLable=QLabel("Текст")
        myLable2=QLabel("Текст2")

        select_file_button=QPushButton('Выбрать файл')
        spectre_button=QPushButton('Показать спектр')
        osc_button=QPushButton('Показать осциллограмму')

        verticalLayout.addWidget(self.myLable)
        verticalLayout.addWidget(select_file_button)
        verticalLayout.addWidget(spectre_button)
        verticalLayout.addWidget(osc_button)
        mainLayout.addWidget(myLable2)

        select_file_button.clicked.connect(self.select_file)

        self.clicks_counter = 0

    def select_file_button_clicked(self):
        print('Нажата кнопка select_file_button')

    def count_clicks(self):
        self.clicks_counter += 1
        self.myLable.setText(f'Количество нажатий на кнопку = {self.clicks_counter}')

    def select_file(self):
        filename, filter = QFileDialog.getOpenFileName()
        self.myLable.setText(f'Выбранный файл: {filename}')



app=QApplication([])
mainWidget = MyWidget()
mainWidget.show()
app.exec()