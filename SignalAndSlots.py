from PyQt5.QtWidgets import QApplication, QPushButton, QMainWindow
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect
from PyQt5 import QtCore

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
        self.show()


    def CreateButton(self):
        button = QPushButton("Click Me", self)
        #button.move(50, 50)
        button.setGeometry(QRect(100, 100, 111, 28))
        button.setIcon(QtGui.QIcon("Icon/python.png"))
        button.setIconSize(QtCore.QSize(30, 30))
        button.setToolTip("<h2>This is click me button!<h2>")
        button.clicked.connect(self.ButtonAction)

    def ButtonAction(self):
         print("Hello World")
         sys.exit()

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())
