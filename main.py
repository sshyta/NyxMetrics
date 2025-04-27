import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout
from ui.ui_main import Ui_MainWindow
from app.core.loaderButton import LoadingFile
from app.core.tableViewer import TableViewer

class NyxMetric(QMainWindow):
    def __init__(self):
        super(NyxMetric, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.ui.home_btn.clicked.connect(self.showHome)
        self.ui.date_btn.clicked.connect(self.showData)
        self.ui.charts_btn.clicked.connect(self.showCharts)
        self.ui.settings_btn.clicked.connect(self.showSettings)
        
        self.table_viewer = TableViewer(self.ui.Data) # Экземпляр класса TableViewer
        self.table_viewer.setGeometry(self.ui.tableView.geometry())
        self.ui.tableView.setParent(None)

        self.file_loader = LoadingFile(self, self.ui.status_label) # Экземпляр класса LoadingFile
        self.ui.uploadButton.clicked.connect(self.file_loader.load_file) # Подключение кнопки к загрузке файлов
        self.ui.clearButton.clicked.connect(self.clear_data_and_lable) # Подключение кнопки очистки данных
        self.file_loader.file_loaded.connect(self.update_table) # Подключение к таблице

    def showHome(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Home)

    def showData(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Data)

    def showCharts(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Charts)

    def showSettings(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.Settings)

    def update_table(self, df):
        self.table_viewer.display_data(df) 

    def clear_data_and_lable(self):
        self.file_loader.clear_lable()
        self.table_viewer.clear_data()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    windows = NyxMetric()
    windows.show()
    sys.exit(app.exec())