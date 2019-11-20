#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout, QComboBox,
                            QTextEdit, QTableView, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class Edits(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #Создание области
        grid = QGridLayout()
        grid.setSpacing(1)
        #Lineedit
        self.set01 = QLineEdit()
        self.set01.setReadOnly(True)
        self.set1 = QLineEdit()
        self.set2 = QComboBox()
        self.set3 = QLineEdit()
        self.set4 = QLineEdit(echoMode=QLineEdit.Password)
        #Label
        self.labl01 = QLabel('ID')
        self.labl1 = QLabel('ФИО')
        self.labl2 = QLabel('Система')
        self.labl3 = QLabel('Логин')
        self.labl4 = QLabel('Пароль')
        #Button
        self.butt1 = QPushButton("&Изменить")
        self.butt2 = QPushButton("&Выйти")
        self.butt2.clicked.connect(self.he)
        #
        #Добавление интерфейса в настройки
        grid.addWidget(self.labl01, 0, 0)
        grid.addWidget(self.labl1, 1, 0)
        grid.addWidget(self.labl2, 2, 0)
        grid.addWidget(self.labl3, 3, 0)
        grid.addWidget(self.labl4, 4, 0)
        
        grid.addWidget(self.set01, 0, 1)
        grid.addWidget(self.set1, 1, 1)
        grid.addWidget(self.set2, 2, 1)
        grid.addWidget(self.set3, 3, 1)
        grid.addWidget(self.set4, 4, 1)
        
        grid.addWidget(self.butt1, 5, 0)
        grid.addWidget(self.butt2, 5, 1)
        #
        self.setLayout(grid)
        #self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('Изменение')
        #self.show()
        
    def he(self):
        self.hide()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Edits()
    sys.exit(app.exec_())
    
    