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
        self.label = QLabel(self)

        self.CreateCheckBox()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.label)

        self.setLayout(vbox)
        self.show()

    def CreateCheckBox(self):
        self.groupBox = QGroupBox("What is your name?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 10))
        hboxLayout = QHBoxLayout()

        self.check1 = QCheckBox("Java")
        self.check1.setIcon(QtGui.QIcon(self.IconName))
        self.check1.setIconSize(QtCore.QSize(40, 40))
        self.check1.toggled.connect(self.OnCheckBox)

        self.check2 = QCheckBox("C++")
        self.check2.setIcon(QtGui.QIcon(self.IconName))
        self.check2.setIconSize(QtCore.QSize(40, 40))
        self.check2.setFont(QtGui.QFont("Sanserif", 10))
        self.check2.toggled.connect(self.OnCheckBox)

        self.check3 = QCheckBox("Python")
        self.check3.setIcon(QtGui.QIcon(self.IconName))
        self.check3.setIconSize(QtCore.QSize(40, 40))
        self.check3.toggled.connect(self.OnCheckBox)

        hboxLayout.addWidget(self.check1)
        hboxLayout.addWidget(self.check2)
        hboxLayout.addWidget(self.check3)

        self.groupBox.setLayout(hboxLayout)

    def OnCheckBox(self):
        if self.check1.isChecked():
            self.label.setText("You have selected : " + self.check1.text())

        elif self.check2.isChecked():
            self.label.setText("You have selected : " + self.check2.text())

        elif self.check3.isChecked():
            self.label.setText("You have selected : " + self.check3.text())


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
