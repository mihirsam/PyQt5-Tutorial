from PyQt5.QtWidgets import QWidget, QSpinBox, QDial, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

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
        self.spinbox = QSpinBox()
        self.spinbox.valueChanged.connect(self.SpinChange)

        vbox.addWidget(self.spinbox)

        self.label = QLabel(self)
        self.label.setAlignment(Qt.AlignCenter)

        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def SpinChange(self):
        spinValue = self.spinbox.value()
        self.label.setText("Value : "+str(spinValue))

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())