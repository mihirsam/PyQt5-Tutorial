from PyQt5.QtWidgets import QMenu, QMessageBox, QFileDialog, QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QFileInfo
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

class Window(QMainWindow):
    def __init__(self, val):
        super().__init__()

        self.title = "Context Menu"
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
    
        self.show()
    

    def contextMenuEvent(self, event):
        contextMenu = QMenu(self)

        newAction = contextMenu.addAction("New")
        openAction = contextMenu.addAction("Open")
        exitAction = contextMenu.addAction("Exit")

        action = contextMenu.exec_(self.mapToGlobal(event.pos()))

        if action ==  exitAction:
            self.close()
    


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())