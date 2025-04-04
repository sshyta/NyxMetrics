import sys
from random import choice
from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow

window_title = [
    "My App",
    "My App",
    "Still My App",
    "Still My App",
    "What on earth",
    "What on earth",
    "This is surprising",
    "This is surprising",
    "Something went wrong",
]


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.n_time_cliked = 0
        
        self.setWindowTitle ('my app')
        
        self.button = QPushButton('Press me!')
        self.button.clicked.connect(self.the_button_was_clicked)
        
        self.windowTitleChanged.connect(self.the_button_was_changed)
        
        self.setCentralWidget(self.button)
    
    def the_button_was_clicked(self):
        print("Clicked.")
        new_window_title = choice(window_title)
        print("Setting title:  %s" % new_window_title)
        self.setWindowTitle(new_window_title)
    
    def the_button_was_changed(self):
        print("window title changed: :  %s" % window_title)

        if window_title == 'Somefing went wrong':
            self.button.setDisabled(True)
            
app = QApplication(sys.argv)

windows = MainWindow()
windows.show()

# Запуск
app.exec()
