from PyQt5.QtWidgets import QListWidget, QDockWidget, QStackedWidget, QTabWidget, QComboBox, QDialogButtonBox, QTabWidget, QMenu, QMessageBox, QFileDialog, QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QFileInfo
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Window(QDialog, QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Second Dialog"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')
    
        vbox = QVBoxLayout()
        self.btn = QPushButton("Forward")
        self.btn.clicked.connect(self.openSecond)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.show()
    
    
    def openSecond(self):
        #App = QApplication(sys.argv)
        self.window = WindowTwo()
        #sys.exit(App.exec())
        self.window.show()
        self.close()

class WindowTwo(QDialog, QWidget):
    def __init__(self):
        super().__init__()

        self.title = "PyQt5 Second Dialog"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')
    
        vbox = QVBoxLayout()
        self.btn = QPushButton("Back")
        self.btn.clicked.connect(self.openFirst)
        vbox.addWidget(self.btn)
        self.setLayout(vbox)

        self.show()

    def openFirst(self):
        #App = QApplication(sys.argv)
        self.window = Window()
        self.window.show()
        self.close()
        #sys.exit(App.exec())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())