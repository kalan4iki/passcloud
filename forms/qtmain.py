#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
from forms import qtset, qtsea, qtadd, qtedit
from PyQt5.QtWidgets import (QMainWindow, QAction, qApp, QApplication, QLineEdit, QLabel,
                            QDesktopWidget, QWidget, QPushButton, QGridLayout,
                            QTextEdit, QTableView, QTableWidget, QTableWidgetItem)
from PyQt5.QtGui import QIcon, QStandardItemModel, QStandardItem
from PyQt5.QtCore import Qt 


class Mainwin(QMainWindow):

    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        #Инициализация окон
        self.Formset = qtset.Sett()
        self.Formsea = qtsea.Search()
        self.Formadd = qtadd.Adds()
        self.Formedit = qtedit.Edits()
        #
        #Центральный виджет интерфейса
        centralWidget = QWidget(self)
        self.setCentralWidget(centralWidget)
        ###Настройки меню
        self.exitAction = QAction(QIcon('exit.png'), '&Выход', self)
        self.exitAction.setShortcut('Ctrl+Q')
        self.exitAction.setStatusTip('Закрыть приложение.')
        self.exitAction.triggered.connect(qApp.quit)
        #
        self.addAction = QAction('&Добавить', self)
        self.addAction.setShortcut('Ctrl+A')
        self.addAction.setStatusTip('Добавить запись.')
        self.addAction.triggered.connect(self.Addform)
        #
        self.conAction = QAction('&Присоединиться', self)
        #conAction.setShortcut('Ctrl+')
        self.conAction.setStatusTip('Присоеденение к базе.')
        #conAction.triggered.connect(self.)
        #
        self.setAction = QAction('&Настройки', self)
        self.setAction.setShortcut('Ctrl+,')
        self.setAction.setStatusTip('Открыть окно настроек.')
        self.setAction.triggered.connect(self.setting)
        #
        self.editAction = QAction('&Редактирование', self)
        self.editAction.setShortcut('Ctrl+E')
        self.editAction.setStatusTip('Открыть окно редактирование записей.')
        self.editAction.triggered.connect(self.Editform)
        #
        self.searthAction = QAction('&Поиск', self)
        self.searthAction.setShortcut('Ctrl+F')
        self.searthAction.setStatusTip('Открыть окно поиска.')
        self.searthAction.triggered.connect(self.Searchform)
        ###Разделение области
        #but = QPushButton('Отправить')
        self.title1 = QLabel('ФИО')
        self.title2 = QLabel('Системы')
        self.title3 = QLabel('Учетная запись')
        self.block2 = QLineEdit()
        self.block2.setAlignment(Qt.AlignTop)
        self.tableFIO = QTableWidget(self)
        self.tableFIO.setColumnCount(1)
        self.tableFIO.setRowCount(1)
        Itemtablefio = QTableWidgetItem('Test row')
        Itemtablefio.setFlags(Qt.ItemIsSelectable | Qt.ItemIsEnabled)
        self.tableFIO.setItem(0, 0, Itemtablefio)
        self.tableSYS = QTableWidget()
        self.tableFIO.itemSelectionChanged.connect(self.testselect)
        grid = QGridLayout()
        grid.setSpacing(1)
        
        #Реализация интерфейса окна
        grid.addWidget(self.title1, 0, 0, alignment=Qt.AlignCenter)
        grid.addWidget(self.title2, 0, 2, alignment=Qt.AlignCenter)
        grid.addWidget(self.title3, 0, 4, alignment=Qt.AlignCenter)
        grid.setColumnMinimumWidth(1, 10)
        grid.setColumnMinimumWidth(3, 10)
        grid.setColumnStretch(0, 2)
        grid.setColumnStretch(2, 2)
        grid.setColumnStretch(4, 2)
        grid.setRowStretch(0, 1)
        grid.setRowStretch(1, 8)
        grid.addWidget(self.tableFIO, 1, 0)
        grid.addWidget(self.tableSYS, 1, 2)
        grid.addWidget(self.block2, 1, 4, alignment=Qt.AlignTop)
        
        ###Реализация статусбара
        self.statusBar()
        self.menubar = self.menuBar()
        fileMenu = self.menubar.addMenu('&Файл')
        file2Menu = self.menubar.addMenu('&Редактирование')
        file2Menu.addAction(self.addAction)
        file2Menu.addAction(self.editAction)
        fileMenu.addAction(self.conAction)
        fileMenu.addAction(self.setAction)
        fileMenu.addAction(self.searthAction)
        fileMenu.addSeparator()
        fileMenu.addAction(self.exitAction)
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
        
    def setting(self):
        self.Formset.setWindowModality(Qt.ApplicationModal) #Чтобы заблокировать основное окно
        self.Formset.show()
    def Searchform(self):
        self.Formsea.setWindowModality(Qt.ApplicationModal)
        self.Formsea.show()
    def Addform(self):
        self.Formadd.setWindowModality(Qt.ApplicationModal)
        self.Formadd.show()
    def Editform(self):
        self.Formedit.setWindowModality(Qt.ApplicationModal)
        self.Formedit.show()
        
    def testselect(self):
        a = self.menubar.actions()[0].text()
        print(a)

    #print(ex.title1)