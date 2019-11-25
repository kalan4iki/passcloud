#from qtmain import Mainwin
import pytest
from pytestqt import qt_compat
from pytestqt.qt_compat import qt_api
from forms import qtset, qtmain, qtsea, qtadd, qtedit
from time import sleep
from PyQt5.QtCore import *
from PyQt5.QtWidgets import qApp

def test_mainform(qtbot):
    window = qtmain.Mainwin()
    
    qtbot.addWidget(window)
    window.show()
    assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    assert window.title1.text() == 'ФИО'
    assert window.menubar.actions()[0].text() == '&Файл'

def test_setform(qtbot):
    window = qtset.Sett()
    
    qtbot.addWidget(window)
    window.show()
    assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    assert window.labl1.text() == 'Setting 1'

def test_seaform(qtbot):
    window = qtsea.Search()
    
    qtbot.addWidget(window)
    window.show()
    assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    assert window.labl1.text() == 'ФИО'
    
def test_addform(qtbot):
    window = qtadd.Adds()
    
    qtbot.addWidget(window)
    window.show()
    assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    assert window.labl1.text() == 'ФИО'
    
    
def test_edit(qtbot):
    window = qtedit.Edits()
    
    qtbot.addWidget(window)
    window.show()
    assert qtbot.waitForWindowShown(window) is True
    sleep(3)
    assert window.labl1.text() == 'ФИО'

    