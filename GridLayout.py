from PyQt5.QtWidgets import QApplication, QPushButton, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Grid Layout!"
        self.left = 500
        self.top = 200
        self.width = 400
        self.height = 100
        self.IconName = "Icon/python.png"

        self.InitWindow()

    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setGeometry(self.left, self.top, self.width, self.height)

        self.CreateLayout()
        self.CreateLayout2()
        vbox = QVBoxLayout()
        vbox.addWidget(self.groupBox)
        vbox.addWidget(self.groupBox2)
        self.setLayout(vbox)
        self.show()


    def CreateLayout(self):
        self.groupBox = QGroupBox("Fav programming language?")
        gridLayout = QGridLayout()

        pythonButton = QPushButton("Python", self)
        #button.move(50, 50)
        pythonButton.setGeometry(QRect(100, 100, 111, 28))
        pythonButton.setIcon(QtGui.QIcon("Icon/python.png"))
        pythonButton.setIconSize(QtCore.QSize(30, 30))
        pythonButton.setMinimumHeight(40)
        pythonButton.clicked.connect(self.ButtonAction)
        gridLayout.addWidget(pythonButton, 0, 0)

        javaButton = QPushButton("Java", self)
        #button.move(50, 50)
        javaButton.setGeometry(QRect(100, 100, 111, 28))
        javaButton.setIcon(QtGui.QIcon("Icon/python.png"))
        javaButton.setIconSize(QtCore.QSize(30, 30))
        javaButton.setMinimumHeight(40)
        javaButton.clicked.connect(self.ButtonAction)
        gridLayout.addWidget(javaButton, 0, 1)

        self.groupBox.setLayout(gridLayout)


    def CreateLayout2(self):
        self.groupBox2 = QGroupBox("Fav programming language?")
        gridLayout = QGridLayout()

        pythonButton = QPushButton("Python", self)
        #button.move(50, 50)
        pythonButton.setGeometry(QRect(100, 100, 111, 28))
        pythonButton.setIcon(QtGui.QIcon("Icon/python.png"))
        pythonButton.setIconSize(QtCore.QSize(30, 30))
        pythonButton.setMinimumHeight(40)
        pythonButton.clicked.connect(self.ButtonAction)
        gridLayout.addWidget(pythonButton, 0, 0)

        javaButton = QPushButton("Java", self)
        #button.move(50, 50)
        javaButton.setGeometry(QRect(100, 100, 111, 28))
        javaButton.setIcon(QtGui.QIcon("Icon/python.png"))
        javaButton.setIconSize(QtCore.QSize(30, 30))
        javaButton.setMinimumHeight(40)
        javaButton.clicked.connect(self.ButtonAction)
        gridLayout.addWidget(javaButton, 0, 1)

        self.groupBox2.setLayout(gridLayout)

    def ButtonAction(self):
         print("Button is clicked")
if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
