from PyQt5.QtWidgets import QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
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
        self.setStyleSheet('background-color:green')


        self.slider = QSlider()
        self.slider.setOrientation(Qt.Horizontal)
        self.slider.setTickPosition(QSlider.TicksBelow)
        self.slider.setTickInterval(10)
        self.slider.setMinimum(0)
        self.slider.setMaximum(100)
        self.slider.valueChanged.connect(self.ChangeValue)

        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        hbox = QHBoxLayout()
        hbox.addWidget(self.slider)
        hbox.addWidget(self.label)
        self.setLayout(hbox)
        self.show()

    def ChangeValue(self):
        size = self.slider.value()
        self.label.setText(str(size))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())