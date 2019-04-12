from PyQt5.QtWidgets import QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "Line Edit"
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

        hbox = QHBoxLayout()

        self.buttonGroup = QButtonGroup()
        
        buttonOne = QPushButton("Python")
        buttonTwo = QPushButton("Java")

        buttonOne.setIcon(QtGui.QIcon(self.IconName))
        buttonOne.setIconSize(QtCore.QSize(40, 40))

        buttonTwo.setIcon(QtGui.QIcon(self.IconName))
        buttonTwo.setIconSize(QtCore.QSize(40, 40))
        
        self.buttonGroup.addButton(buttonOne)
        self.buttonGroup.addButton(buttonTwo)
        self.buttonGroup.buttonClicked[int].connect(self.OnButtonClick)

        self.label = QLabel(self)

        hbox.addWidget(buttonOne)
        hbox.addWidget(buttonTwo)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
        
        self.show()


    def OnButtonClick(self, id):
        for button in self.buttonGroup.buttons():
            if button is self.buttonGroup.button(id):
                self.label.setText(button.text() + " is clicked!")
            
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())