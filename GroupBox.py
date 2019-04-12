from PyQt5.QtWidgets import QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
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

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        groupbox = QGroupBox("Select your favourite fruit?")
        groupbox.setFont(QtGui.QFont("Sanserif", 10))

        hbox = QHBoxLayout()
        hbox.addWidget(groupbox)

        vbox = QVBoxLayout()

        rad1 = QRadioButton("Python")
        vbox.addWidget(rad1)

        rad2 = QRadioButton("Java")
        vbox.addWidget(rad2)

        groupbox.setLayout(vbox)
        self.setLayout(hbox)
        
        self.show()
            
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())