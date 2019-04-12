from PyQt5.QtWidgets import QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "QGroup  Box"
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
        self.setStyleSheet('background-color:yellow')

        hbox = QHBoxLayout()
        
        self.frame = QFrame()
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setLineWidth(0.6)
        self.frame.setStyleSheet('background-color:'+self.color)

        button = QPushButton("Change Color")
        button.setStyleSheet('color:White')
        button.clicked.connect(self.ChangeColor)
        button.setStyleSheet('background-color:green')


        hbox.addWidget(self.frame)
        hbox.addWidget(button)

        self.setLayout(hbox)
        self.show()

    def ChangeColor(self):
        if self.color == 'red':
            self.color = 'green'
            self.frame.setStyleSheet('background-color:'+self.color)
        else:
            self.color = 'red'
            self.frame.setStyleSheet('background-color:'+self.color)
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())