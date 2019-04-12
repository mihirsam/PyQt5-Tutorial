from PyQt5.QtWidgets import QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
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

        
        self.lineedit = QLineEdit(self)
        self.lineedit.setFont(QtGui.QFont("Sanserif", 15))
        self.lineedit.returnPressed.connect(self.OnPressed)
        
        self.label = QLabel(self)
        self.label.setFont(QtGui.QFont("Sanserif", 15))
    
        hbox = QHBoxLayout()
        hbox.addWidget(self.lineedit)
        hbox.addWidget(self.label)

        self.setLayout(hbox)
        self.show()


    def OnPressed(self):
        self.label.setText(self.lineedit.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())