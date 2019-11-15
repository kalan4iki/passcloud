#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout,
                            QTextEdit, QTableView, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

class Sett(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()


    def initUI(self):
        #Создание области
        grid = QGridLayout()
        grid.setSpacing(1)
        #Lineedit
        set1 = QLineEdit()
        set2 = QLineEdit()
        set3 = QLineEdit()
        #Label
        labl1 = QLabel('Setting 1')
        labl2 = QLabel('Setting 2')
        labl3 = QLabel('Setting 3')
        #Button
        butt1 = QPushButton("&Сохранить")
        butt2 = QPushButton("Выйти")
        butt2.clicked.connect(self.he)
        #
        #Добавление интерфейса в настройки
        grid.addWidget(labl1, 0, 0)
        grid.addWidget(labl2, 1, 0)
        grid.addWidget(labl3, 2, 0)
        
        grid.addWidget(set1, 0, 1)
        grid.addWidget(set2, 1, 1)
        grid.addWidget(set3, 2, 1)
        
        grid.addWidget(butt1, 3, 0)
        grid.addWidget(butt2, 3, 1)
        #
        self.setLayout(grid)
        #self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('Настройки')
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
    ex = Sett()
    sys.exit(app.exec_())
    
    