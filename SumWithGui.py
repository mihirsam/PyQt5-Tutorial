from PyQt5.QtWidgets import QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "Sum"
        self.left = 100
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()


    def CreateLayout(self):
        #self.groupbox = QGroupBox("Find the sum of two numbers!")

        hboxOne = QHBoxLayout()
        labelOne = QLabel("Enter Number One : ")
        self.lineEditOne = QLineEdit()

        hboxOne.addWidget(labelOne)
        hboxOne.addWidget(self.lineEditOne)

        hboxTwo = QHBoxLayout()
        labelTwo = QLabel("Enter Number Two : ")
        self.lineEditTwo = QLineEdit()

        hboxTwo.addWidget(labelTwo)
        hboxTwo.addWidget(self.lineEditTwo)

        sumButton = QPushButton("Calculate")
        sumButton.setFont(QtGui.QFont("Sanserif", 10))
        sumButton.setToolTip("Calculate Sum Of Two Numbers!")
        sumButton.clicked.connect(self.CalculateSum)

        self.label = QLabel(self)

        vbox = QVBoxLayout()
        vbox.addLayout(hboxOne)
        vbox.addLayout(hboxTwo)
        vbox.addWidget(sumButton)
        vbox.addWidget(self.label)

        #self.groupbox.setLayout(vbox)
        self.setLayout(vbox)
        self.show()


    def CalculateSum(self):
        self.label.setText("Sum = " + "{}" .format(int(self.lineEditOne.text()) + int(self.lineEditTwo.text())))
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())