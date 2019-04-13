from PyQt5.QtWidgets import QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap

class Window(QDialog):
    def __init__(self, val):
        super().__init__()

        self.title = "QGroup  Box"
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

        self.button = QPushButton()
        self.button.clicked.connect(self.onClicked)
        
        formLayout = QFormLayout()
        groupBox = QGroupBox("This Is GroupBox")

        labelList = []
        buttonList = []

        for i  in range(self.val):
            labelList.append(QLabel("label"+str(i)))
            buttonList.append(QPushButton("Button "+str(i)))
            formLayout.addRow(labelList[i], buttonList[i])

        groupBox.setLayout(formLayout)
        scroll = QScrollArea()
        scroll.setWidget(groupBox)
        scroll.setWidgetResizable(True)
        scroll.setFixedHeight(400)


        layout = QVBoxLayout()
        layout.addWidget(scroll)

        self.setLayout(layout)

        self.show()

    def onClicked(self):
        print(self.button.text())

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Window(20)
    sys.exit(App.exec())