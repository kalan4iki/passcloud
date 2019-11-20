#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout,
                            QTextEdit, QTableView, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class Search(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #Создание области
        grid = QGridLayout()
        grid.setSpacing(1)
        #Lineedit
        self.set1 = QLineEdit()
        #Label
        self.labl1 = QLabel('ФИО')
        #Button
        self.butt1 = QPushButton("&Поиск")
        self.butt2 = QPushButton("&Выйти")
        self.butt2.clicked.connect(self.he)
        #
        #Добавление интерфейса в настройки
        grid.addWidget(self.labl1, 0, 0)
        
        grid.addWidget(self.set1, 0, 1)
        
        grid.addWidget(self.butt1, 3, 0)
        grid.addWidget(self.butt2, 3, 1)
        #
        self.setLayout(grid)
        #self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('Поиск')
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
    ex = Search()
    sys.exit(app.exec_())
    
    