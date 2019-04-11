from PyQt5.QtWidgets import QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore


class Window(QDialog):

    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Labelling!"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 400
        self.IconName = "Icon/python.png"

        self.InitWindow()


    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

        vbox = QVBoxLayout()
        label = QLabel("This is PyQt5 Label")
        label2 = QLabel("This PyQt5 Label")
        label2.setFont(QtGui.QFont("Sanserif ", 20))
        label2.setStyleSheet('color:red')
        vbox.addWidget(label)
        vbox.addWidget(label2)

        self.setLayout(vbox)
        self.show()


if  __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
