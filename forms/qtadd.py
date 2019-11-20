#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout, QComboBox,
                            QTextEdit, QTableView, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class Adds(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        #Создание области
        grid = QGridLayout()
        grid.setSpacing(1)
        #Lineedit
        self.set1 = QLineEdit()
        self.set2 = QComboBox()
        self.set3 = QLineEdit()
        self.set4 = QLineEdit(echoMode=QLineEdit.Password)
        #Label
        self.labl1 = QLabel('ФИО')
        self.labl2 = QLabel('Система')
        self.labl3 = QLabel('Логин')
        self.labl4 = QLabel('Пароль')
        #Button
        self.butt1 = QPushButton("&Добавить")
        self.butt2 = QPushButton("&Выйти")
        self.butt2.clicked.connect(self.he)
        #
        #Добавление интерфейса в настройки
        grid.addWidget(self.labl1, 0, 0)
        grid.addWidget(self.labl2, 1, 0)
        grid.addWidget(self.labl3, 2, 0)
        grid.addWidget(self.labl4, 3, 0)
        grid.addWidget(self.set1, 0, 1)
        grid.addWidget(self.set2, 1, 1)
        grid.addWidget(self.set3, 2, 1)
        grid.addWidget(self.set4, 3, 1)
        grid.addWidget(self.butt1, 4, 0)
        grid.addWidget(self.butt2, 4, 1)
        #
        self.setLayout(grid)
        self.center()    
        self.setWindowTitle('Поиск')
        
    def he(self):
        self.hide()
    
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())
    