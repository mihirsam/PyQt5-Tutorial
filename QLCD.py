from PyQt5.QtWidgets import QLCDNumber, QWidget, QSpinBox, QDial, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
from random import randint

class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.title = "QDial"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')

        vbox = QVBoxLayout()
        self.lcd = QLCDNumber()
        self.lcd.setStyleSheet('background-color:green')
        #self.lcd.setStyleSheet('color:black')

        self.button = QPushButton("Random Number")
        self.button.clicked.connect(self.RandomGen)
        self.button.setStyleSheet('background-color:red')

        vbox.addWidget(self.lcd)
        vbox.addWidget(self.button)

        self.setLayout(vbox)
        
        self.show()

    def RandomGen(self):
        self.lcd.display(randint(10, 100))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())