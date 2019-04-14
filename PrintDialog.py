from PyQt5.QtWidgets import QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog

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

        colorAction = QAction(QIcon(self.IconName), "Color", self)
        colorAction.setShortcut("Ctrl+d")
        colorAction.triggered.connect(self.fontDialog)

        fontAction = QAction(QIcon(self.IconName), "Font", self)
        fontAction.setShortcut("Ctrl+F")
        fontAction.triggered.connect(self.colorDialog)

        printAction = QAction(QIcon(self.IconName), "Print", self)
        printAction.triggered.connect(self.printDialog)

        viewMenu.addAction(colorAction)
        viewMenu.addAction(printAction)
        
        self.toolbar = self.addToolBar("Toolbar")
        self.toolbar.addAction(cutAction)
        self.toolbar.addAction(pasteAction)
        self.toolbar.addAction(copyAction)
        self.toolbar.addAction(fontAction)
        self.toolbar.addAction(colorAction)

    def fontDialog(self):
        font, ok = QFontDialog.getFont()
        
        if ok:
            self.textEdit.setFont(font)

    def colorDialog(self):
        color = QColorDialog.getColor()
        self.textEdit.setTextColor(color)

    def exitMenu(self):
        self.close()

    def CreateEditor(self):
        self.textEdit = QTextEdit()
        self.setCentralWidget(self.textEdit)

    def printDialog(self):
        printer = QPrinter(QPrinter.HighResolution)
        dialog = QPrintDialog(printer, self)

        if dialog.exec_() == QPrintDialog.Accepted:
            self.textEdit.print_(printer)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())