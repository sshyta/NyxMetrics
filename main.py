import sys
from PyQt6.QtWidgets import QApplication, QMainWindow
from ui.ui_main import Ui_MainWindow
from app.core.loaderButton import LoadingFile
from app.core.tableViewer import TableViewer

class NyxMetric(QMainWindow):
    def __init__(self):
        super(NyxMetric, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)
        
        self.table_viewer = TableViewer(self.ui.centralwidget) # Экземпляр класса TableViewer
        self.table_viewer.setGeometry(self.ui.tableView.geometry())
        self.ui.tableView.setParent(None)
        
        
        self.file_loader = LoadingFile(self, self.ui.status_label) # Экземпляр класса LoadingFile
        self.ui.pushButton.clicked.connect(self.file_loader.load_file) # Подключение кнопки к загрузке файлов
        self.file_loader.file_loaded.connect(self.update_table) # Подключение к таблице
        
    def update_table(self, df):
        self.table_viewer.display_data(df)   
        
        
if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = NyxMetric()
    windows.show()
    sys.exit(app.exec())