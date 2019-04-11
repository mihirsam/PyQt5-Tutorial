from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
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
        self.setWindowTitle("Add Images!")
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setGeometry(self.left, self.top, self.width, self.height)


        vbox = QVBoxLayout()
        labelImage = QLabel(self)
        pixmap = QPixmap(self.IconName)
        labelImage.setPixmap(pixmap)
        
        vbox.addWidget(labelImage)
        self.setLayout(vbox)
        self.show()


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
