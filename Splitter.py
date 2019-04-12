from PyQt5.QtWidgets import QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
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
        leftFrame = QFrame()
        leftFrame.setFrameShape(QFrame.StyledPanel)

        bottomFrame = QFrame()
        bottomFrame.setFrameShape(QFrame.StyledPanel)

        splitterOne = QSplitter(Qt.Horizontal)
        lineEdit = QLineEdit()

        splitterOne.addWidget(leftFrame)
        splitterOne.addWidget(lineEdit)
        splitterOne.setSizes([200, 200])

        splitterTwo = QSplitter(Qt.Vertical)
        lineEdit = QLineEdit()

        splitterTwo.addWidget(splitterOne)
        splitterTwo.addWidget(bottomFrame)
        splitterTwo.setSizes([200, 200])

        hbox.addWidget(splitterTwo)
        self.setLayout(hbox)
        self.show()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())