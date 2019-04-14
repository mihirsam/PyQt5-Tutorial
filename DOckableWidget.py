from PyQt5.QtWidgets import QListWidget, QDockWidget, QStackedWidget, QTabWidget, QComboBox, QDialogButtonBox, QTabWidget, QMenu, QMessageBox, QFileDialog, QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QFileInfo
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Window(QMainWindow):
    def __init__(self):
        super().__init__()

        self.title = "Context Menu"
        self.left = 300
        self.top = 100
        self.width = 500
        self.height = 500
        self.IconName = "Icon/python.png"
        self.color = 'red'

        self.createDockWidget()
        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green')
    
        self.show()
    
    def createDockWidget(self):
        menubar = self.menuBar()
        file = menubar.addMenu("File")

        file.addAction("New")
        file.addAction("Save")
        file.addAction("Close")


        self.dock = QDockWidget("Dockable", self)
        self.listwidget = QListWidget()

        list = ["Python", "Java", "C++", "C#"]

        self.listwidget.addItems(list)

        self.dock.setWidget(self.listwidget)
        self.setCentralWidget(QTextEdit())

        self.addDockWidget(Qt.RightDockWidgetArea, self.dock)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())