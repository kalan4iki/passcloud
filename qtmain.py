#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout,
                            QTextEdit, QTableView)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt

def testselect():
    print('Test select')


class Example(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        ###Настройки меню
        #
        exitAction = QAction(QIcon('exit.png'), '&Выход', self)
        exitAction.setShortcut('Ctrl+Q')
        exitAction.setStatusTip('Закрыть приложение.')
        exitAction.triggered.connect(qApp.quit)
        #
        setAction = QAction('&Настройки', self)
        setAction.setShortcut('Ctrl+,')
        setAction.setStatusTip('Открыть окно настроек.')
        #
        searthAction = QAction('&Поиск', self)
        searthAction.setShortcut('Ctrl+F')
        searthAction.setStatusTip('Открыть окно поиска.')
        #
        ###Разделение области
        #but = QPushButton('Отправить')
        title1 = QLabel('ФИО')
        title2 = QLabel('Системы')
        title3 = QLabel('Учетная запись')
        block2 = QLineEdit()
        block2.setAlignment(Qt.AlignTop)
        tableFIO = QTableView()
        tableSYS = QTableView()
        tableFIO.itemSelectionChanged.connect(testselect)
        #tableFIO.setColumnCount(1)
        #tableSYS.setColumnCount(1)
        grid = QGridLayout()
        grid.setSpacing(1)
        
        NpTableModel = QStandardItemModel(parent=self)
        NpTableModel.appendRow([QStandardItem('qwe')])
        tableFIO.setModel(NpTableModel)
        
        grid.addWidget(title1, 0, 0, alignment=Qt.AlignCenter)
        grid.addWidget(title2, 0, 2, alignment=Qt.AlignCenter)
        grid.addWidget(title3, 0, 4, alignment=Qt.AlignCenter)
        #grid.setRowStretch(0, 0)
        grid.setColumnMinimumWidth(1, 10)
        grid.setColumnMinimumWidth(3, 10)
        #grid.setColumnMinimumWidth()
        grid.setColumnStretch(0, 2)
        grid.setColumnStretch(2, 2)
        grid.setColumnStretch(4, 2)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 8)
        #grid.setRowStretch(2, 1)
        grid.addWidget(tableFIO, 1, 0)
        grid.addWidget(tableSYS, 1, 2)
        grid.addWidget(block2, 1, 4, alignment=Qt.AlignTop)
        
        #grid.addWidget(but, 2, 0, 1, 5)
        ###Реализация статусбара
        self.statusBar()
        menubar = self.menuBar()
        fileMenu = menubar.addMenu('&Файл')
        fileMenu.addAction(setAction)
        fileMenu.addAction(searthAction)
        fileMenu.addSeparator()
        fileMenu.addAction(exitAction)
        #self.statusBar().showMessage('Приложение готово к работе.')
        ###
        centralWidget.setLayout(grid)
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
    ex = Example()
    sys.exit(app.exec_())