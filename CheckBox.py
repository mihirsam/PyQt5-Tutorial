from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap



class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "CheckBox"
        self.left = 300
        self.top = 400
        self.width = 400
        self.height = 100
        self.IconName = "Icon/python.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateCheckBox()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        
        self.setLayout(vbox)
        self.show()

    def CreateCheckBox(self):
        self.groupBox = QGroupBox("What is your name?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 10))
        hboxLayout = QHBoxLayout()

        self.check1 = QCheckBox("Python")
        self.check1.setIcon(QtGui.QIcon(self.IconName))
        self.check1.setIconSize(QtCore.QSize(40, 40))

        hboxLayout.addWidget(self.check1)

        self.groupBox.setLayout(hboxLayout)



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
