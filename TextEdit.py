from PyQt5.QtWidgets import QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon

class Window(QMainWindow):
    def __init__(self, val):
        super().__init__()

        self.title = "QTextEdit"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'
        self.val = val

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')
        self.CreateEditor()
        self.CreateMenu()
        self.show()
    

    def CreateMenu(self):
        mainMenu = self.menuBar()
        fileMenu = mainMenu.addMenu("File")
        editMenu = mainMenu.addMenu("Edit")
        viewMenu = mainMenu.addMenu("View")
        helpMenu = mainMenu.addMenu("Help")

        copyAction = QAction(QIcon(self.IconName), 'Copy', self)
        pasteAction = QAction(QIcon(self.IconName), 'Paste', self)
        cutAction = QAction(QIcon(self.IconName), 'Cut', self)
        
        copyAction.setShortcut("Ctrl+c")
        
        fileMenu.addAction(copyAction)
        fileMenu.addAction(cutAction)
        fileMenu.addAction(pasteAction)

        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(copyAction)

    def exitMenu(self):
        self.close()

    def CreateEditor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())