from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):

    def __init__(self):

        super().__init__()

        self.title = "PyQt5 Layout Management"
        self.left = 500
        self.top = 500
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"

        self.InitWindow()


    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.createLayout()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        self.setLayout(vbox)

        self.show()

    def  createLayout(self):
        self.groupBox = QGroupBox("What is your favourite Language?")
        hboxlayout = QHBoxLayout()

        pythonButton = QPushButton("Python", self)
        #button.move(50, 50)
        pythonButton.setGeometry(QRect(100, 100, 111, 28))
        pythonButton.setIcon(QtGui.QIcon("Icon/python.png"))
        pythonButton.setIconSize(QtCore.QSize(30, 30))
        pythonButton.setMinimumHeight(40)
        pythonButton.clicked.connect(self.ButtonAction)
        hboxlayout.addWidget(pythonButton)

        javaButton = QPushButton("Java", self)
        #button.move(50, 50)
        javaButton.setGeometry(QRect(100, 100, 111, 28))
        javaButton.setIcon(QtGui.QIcon("Icon/python.png"))
        javaButton.setIconSize(QtCore.QSize(30, 30))
        javaButton.setMinimumHeight(40)
        javaButton.clicked.connect(self.ButtonAction)
        hboxlayout.addWidget(javaButton)

        self.groupBox.setLayout(hboxlayout)

    def ButtonAction(self):
         print("Button is clicked")
         #sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
