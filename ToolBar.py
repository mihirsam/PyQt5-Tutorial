from PyQt5.QtWidgets import QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

class Window(QWidget):
    def __init__(self, val):
        super().__init__()

        self.title = "QGroup  Box"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'
        self.val = val

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')

        vbox = QVBoxLayout()
        toolbox = QToolBox()
        toolbox.setStyleSheet('background-color:green')
        self.label = QLabel()
        self.label2 = QLabel()
        self.label3 = QLabel()

        toolbox.addItem(self.label, "Python")
        toolbox.addItem(self.label2, "Java")
        toolbox.addItem(self.label3, "C++")
        vbox.addWidget(toolbox)

        self.setLayout(vbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())