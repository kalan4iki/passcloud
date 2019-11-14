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
        #
        
        self.resize(600, 400)
        self.center()
        
        self.setWindowTitle('Password cloud')
        self.show()
        
    def center(self):
        qr = self.frameGeometry()
        cp = QDesktopWidget().availableGeometry().center()
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = Sett()
    sys.exit(app.exec_())
    
    