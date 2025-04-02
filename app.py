import sys
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow, QSize


class MainWindow (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('my app')
        button = QPushButton('Pushh')
        self.setCentralWidget(button)

app = QApplication(sys.argv)

windows = MainWindow()
windows.show()

# Запуск
app.exec()