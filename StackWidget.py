from PyQt5.QtWidgets import QStackedWidget, QTabWidget, QComboBox, QDialogButtonBox, QTabWidget, QMenu, QMessageBox, QFileDialog, QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QFileInfo
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog


class Window(QWidget):
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
    
        self.StackedWidget()
        self.show()
    
    def StackedWidget(self):
        vbox = QVBoxLayout()

        self.stackedwidget = QStackedWidget()
        vbox.addWidget(self.stackedwidget)

        for x in range(0, 8):
            label = QLabel("Stacked Child " + str(x))
            label.setFont(QtGui.QFont("Sanserif", 15))
            label.setStyleSheet('color:red')

            self.stackedwidget.addWidget(label)

            self.button = QPushButton("Stack " + str(x))
            self.button.setStyleSheet('background-color:green')
            self.button.page = x
            self.button.clicked.connect(self.btn_clicked)

            vbox.addWidget(self.button)

        self.setLayout(vbox)

    def btn_clicked(self):
        self.button = self.sender()
        self.stackedwidget.setCurrentIndex(self.button.page)


if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())