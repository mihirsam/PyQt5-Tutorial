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

        self.title = "Context Menu"
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
        list = ["python", "C++", "Java"]

        self.combo = QComboBox()
        self.combo.addItem("Python")
        self.combo.addItem("C++")
        self.combo.addItem("Java")
        self.combo.addItems(list)
        self.combo.currentTextChanged.connect(self.comboChanged)
        self.label = QLabel("Hello")
        self.setFont(QtGui.QFont("Sanserif", 15))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.combo)
        vbox.addWidget(self.label)

        self.setLayout(vbox)

        self.show()
    

    def comboChanged(self):
        text = self.combo.currentText()
        self.label.setText("You have selected : " +  text)
    

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())