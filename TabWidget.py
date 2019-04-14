from PyQt5.QtWidgets import QTabWidget, QComboBox, QDialogButtonBox, QTabWidget, QMenu, QMessageBox, QFileDialog, QColorDialog, QFontDialog, QTextEdit, QAction, QMainWindow, QMenuBar, QWidget, QToolBox, QFormLayout, QScrollArea, QSlider, QSplitter, QFrame, QSizeGrip, QRadioButton, QButtonGroup, QLineEdit, QApplication, QPushButton, QLabel, QDialog, QGroupBox, QHBoxLayout, QVBoxLayout, QGridLayout, QCheckBox
import sys
from PyQt5 import QtGui
from PyQt5.QtCore import QRect, Qt, QFileInfo
from PyQt5 import QtCore
from PyQt5.QtGui import  QPixmap, QIcon
from PyQt5.QtPrintSupport import QPrinter, QPrintDialog, QPrintPreviewDialog

class Tab(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt5 tab widget!")
        self.setWindowIcon(QIcon("Icon/python.png"))

        vbox = QVBoxLayout()
        tabWidget = QTabWidget()

        tabWidget.addTab(TabContact(), "Contact Details!")
        tabWidget.addTab(TabPersonDetails(), "Person Details")

        buttonBox = QDialogButtonBox(QDialogButtonBox.Ok | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.accept)
        buttonBox.accepted.connect(self.reject)

        vbox.addWidget(tabWidget)
        vbox.addWidget(buttonBox)

        self.setLayout(vbox)

class TabPersonDetails(QWidget):
    def __init__(self):
        super().__init__()

        groupBox = QGroupBox("Select Your gender!")

        list = ["Male", "Female"]

        combo = QComboBox()
        combo.addItems(list)

        vbox = QVBoxLayout()
        vbox.addWidget(combo)
        groupBox.setLayout(vbox)

        groupbox2 = QGroupBox()
        python = QCheckBox("Python")
        cpp = QCheckBox("C++")
        java = QCheckBox("Java")

        vbox2 = QVBoxLayout()
        vbox2.addWidget(python)
        vbox2.addWidget(cpp)
        vbox2.addWidget(java)
        groupbox2.setLayout(vbox2)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(groupBox)
        mainLayout.addWidget(groupbox2)
        
        self.setLayout(mainLayout)

class TabContact(QWidget):
    def __init__(self):
        super().__init__()

        nameLabel = QLabel("Name : ")
        nameEdit = QLineEdit()

        phoneLabel = QLabel("Phone : ")
        phoneEdit = QLineEdit()

        emailLabel = QLabel("Email : ")
        emailEdit = QLineEdit()

        vbox = QVBoxLayout()
        vbox.addWidget(nameLabel)
        vbox.addWidget(nameEdit)
        vbox.addWidget(phoneLabel)
        vbox.addWidget(phoneEdit)
        vbox.addWidget(emailLabel)
        vbox.addWidget(emailEdit)

        self.setLayout(vbox)

if __name__ == "__main__":
    App = QApplication(sys.argv)
    window = Tab()
    window.show()
    sys.exit(App.exec())