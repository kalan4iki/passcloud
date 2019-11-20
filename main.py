import sys
from forms import qtmain, qtset
from PyQt5.QtWidgets import QApplication

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = qtmain.Mainwin()
    sys.exit(app.exec_())