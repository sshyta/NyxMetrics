import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QWidget, QPushButton, QMainWindow


class MainWindow (QMainWindow):
    def __init__ (self):
        super().__init__()
        self.setWindowTitle('my app')
        button = QPushButton('Pushh')
        self.setFixedSize(QSize(400, 300))
        self.setCentralWidget(button)

app = QApplication(sys.argv)

windows = MainWindow()
windows.show()

# Запуск
app.exec()