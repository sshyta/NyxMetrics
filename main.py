import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
from app.core.loaderButton import LoadingFile

class NyxMetric(QMainWindow):
    def __init__(self):
        super(NyxMetric, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        
        self.file_loader = LoadingFile(self)
        self.ui.pushButton.clicked.connect(self.file_loader.load_file)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = NyxMetric()
    windows.show()
    
    sys.exit(app.exec())