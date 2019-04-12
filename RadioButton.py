from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QRadioButton
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap


class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt Image"
        self.left = 500
        self.top = 200
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle("Radio Button!")
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.RadioButton()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)

        self.label = QLabel(self)
        vbox.addWidget(self.label)
        self.label.setFont(QtGui.QFont("Sanserif", 15))

        self.setLayout(vbox)
        self.show()

    def RadioButton(self):
        self.groupBox = QGroupBox("What is your name?")
        self.groupBox.setFont(QtGui.QFont("Sanserif", 10))

        hboxLayout = QHBoxLayout()
        self.radiobutton1 = QRadioButton("Mihir")
        self.radiobutton1.setChecked(True)
        self.radiobutton1.setIcon(QtGui.QIcon(self.IconName))
        self.radiobutton1.setIconSize(QtCore.QSize(40, 40))
        self.radiobutton1.setFont(QtGui.QFont("Sanserif", 10))
        self.radiobutton1.toggled.connect(self.OnRadioButton)

        self.radiobutton2 = QRadioButton("Not Mihir")
        self.radiobutton2.setChecked(False)
        self.radiobutton2.setIcon(QtGui.QIcon(self.IconName))
        self.radiobutton2.setIconSize(QtCore.QSize(40, 40))
        self.radiobutton2.setFont(QtGui.QFont("Sanserif", 10))
        self.radiobutton2.toggled.connect(self.OnRadioButton)

        hboxLayout.addWidget(self.radiobutton1)
        hboxLayout.addWidget(self.radiobutton2)
        self.groupBox.setLayout(hboxLayout)


    def OnRadioButton(self):
        radioButton = self.sender()

        if radioButton.isChecked():
            self.label.setText("You have selected " + radioButton.text())



if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
