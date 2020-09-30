import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QMessageBox, QShortcut

from BotClick import clicker


class AutoGui(QMainWindow):

    def __init__(self):
        super().__init__()
        uic.loadUi('GUI_autoclick.ui', self)
        self.Start_Button.pressed.connect(self.enterPress)
        self.Stop_Button.pressed.connect(self.enterPress)
        self.shortcut = QShortcut("F6", self)
        self.shortcut.activated.connect(self.enterPress)
        self.validation = False
        self.click1 = clicker()

        self.lineEdit_min.setRange(0, 60)
        self.lineEdit_sec.setRange(0, 60)
        self.lineEdit_msec.setRange(0, 60)

    def enterPress(self):
        self.validation = False if self.validation else True

        if self.lineEdit_min.value() <= 0 and self.lineEdit_sec.value() <= 0 and self.lineEdit_msec.value() <= 0:
            self.show_dialog()
        else:
            self.switchButton()

            delay = self.lineEdit_msec.value() / 1000 + self.lineEdit_sec.value() + self.lineEdit_min.value() * 60

            if (self.validation):
                self.click1.start_clicking(delay)
            else:
                self.click1.stop_clicking()

    def switchButton(self):
        self.Start_Button.setEnabled(False if self.Start_Button.isEnabled() else True)
        self.Stop_Button.setEnabled(False if self.Stop_Button.isEnabled() else True)

    def show_dialog(self):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText("Input fields cannot have negative or empty values")
        msg.setWindowTitle("Error in the input field")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    file = open("Styles/default.qss", 'r')
    with file:
        qss = file.read()
        app.setStyleSheet(qss)
    GUI = AutoGui()
    GUI.show()
    sys.exit(app.exec_())
