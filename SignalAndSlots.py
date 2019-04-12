from PyQt5.QtWidgets import QHBoxLayout, QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore
from functools import partial

def PButton(string):
        print(string)
        
class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        title = "PyQt5 Push Button"
        left = 500
        top = 500
        width = 500
        height = 500
        IconName = "Icon/python.png"

        self.setWindowTitle(title)
        self.setWindowIcon(QtGui.QIcon(IconName))
        self.setGeometry(left, top, width, height)

        self.CreateButton()
        

    def CreateButton(self):
        button = QPushButton("Click Me", self)
        #button.move(50, 50)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon("Icon/python.png"))
        button.setIconSize(QtCore.QSize(30, 30))
        button.setToolTip("<h2>This is click me button!<h2>")
        button.clicked.connect(self.ButtonAction)

        buttonTwo = QPushButton("Partial", self)
        #button.move(50, 50)
        buttonTwo.setGeometry(QRect(100, 200, 111, 28))
        buttonTwo.setIcon(QtGui.QIcon("Icon/python.png"))
        buttonTwo.setIconSize(QtCore.QSize(30, 30))
        buttonTwo.setToolTip("<h2>This is click me button!<h2>")
        buttonTwo.clicked.connect(partial(PButton, "This is Partial!"))

        hbox = QHBoxLayout()
        hbox.addWidget(button)
        hbox.addWidget(buttonTwo)

        self.setLayout(hbox)
        self.show()

    def ButtonAction(self):
         print("Hello World")
         #sys.exit()

    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
