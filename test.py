#from qtmain import Mainwin
import pytest
from passcloud.qtmain import Mainwin
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import qApp

def test_myapp(qtbot):
    window = Mainwin()
    
    qtbot.addWidget(window)
    window.show()
    #assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    #qtbot.mouseClick(window.menubar.actions()[0], Qt.LeftButton)
    assert window.title1.text() == 'ФИО'
    assert window.menubar.actions()[0].text() == '&Файл'
