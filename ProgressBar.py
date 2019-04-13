from PyQt5.QtWidgets import QProgressBar, QWidget, QSpinBox, QDial, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QThread, pyqtSignal
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap
import time


class MyThread(QThread):
    change_value = pyqtSignal(int)

    def run(self):
        count = 0

        while count < 100:
            count += 1

            time.sleep(0.3)
            self.change_value.emit(count)

class Window(QDialog):
    def __init__(self):
        super().__init__()

        self.title = "QPRogressBar"
        self.left = 300
        self.top = 100
        self.width = 300
        self.height = 100
        self.IconName = "Icon/python.png"
        self.color = 'red'

        self.InitWindow()

    def InitWindow(self):
        self.setWindowIcon(QtGui.QIcon(self.IconName))
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)
        #self.setStyleSheet('background-color:green'
        
        self.progressbar = QProgressBar()
        self.progressbar.setStyleSheet("QProgressBar {border: 2px solid grey; border-radius: 8px; padding: 1px}"
                                        "QProgressBar::chunk {background : green}")
        self.progressbar.setTextVisible(False)
        self.progressbar.setOrientation(Qt.Vertical)

        self.button = QPushButton("Run Progressbar")
        self.button.clicked.connect(self.startProrgessBar)
        self.button.setStyleSheet('background-color:yellow')

        vbox = QVBoxLayout()
        vbox.addWidget(self.progressbar)
        vbox.addWidget(self.button)

        self.setLayout(vbox)
        self.show()

   
    def startProrgessBar(self):
       self.thread = MyThread()
       self.thread.change_value.connect(self.setProgressVal)
       self.thread.start()

    def setProgressVal(self, val):
        self.progressbar.setValue(val)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window()
    sys.exit(App.exec())