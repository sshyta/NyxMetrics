import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QMessageBox
from ui.ui_main import Ui_MainWindow
from app.core.loaderButton import LoadingFile
from app.core.tableViewer import TableViewer
from app.core.check_db import *
from app.core.handler.db_handler import *

class NyxMetric(QMainWindow):
    def __init__(self):
        super(NyxMetric, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.retranslateUi(self)

        self.ui.stackedWidget.setCurrentIndex(0)

        self.hide_menu_buttons()

        # подключение кнопок меню
        self.ui.home_btn.clicked.connect(self.showHome)
        self.ui.date_btn.clicked.connect(self.showData)
        self.ui.charts_btn.clicked.connect(self.showCharts)
        self.ui.settings_btn.clicked.connect(self.showSettings)
        
        # таблица с данными
        self.table_viewer = TableViewer(self.ui.Data) # Экземпляр класса TableViewer
        self.table_viewer.setGeometry(self.ui.tableView.geometry())
        self.ui.tableView.setParent(None)

        # загрузчик 
        self.file_loader = LoadingFile(self, self.ui.status_label) # Экземпляр класса LoadingFile
        self.ui.uploadButton.clicked.connect(self.file_loader.load_file) # Подключение кнопки к загрузке файлов
        self.ui.clearButton.clicked.connect(self.clear_data_and_lable) # Подключение кнопки очистки данных
        self.file_loader.file_loaded.connect(self.update_table) # Подключение к таблице

        # экземпляр класса 
        self.check_db = CheckThread()
        self.check_db.mysignal.connect(self.signal_handler)

        # обработка кнопок экрана с регистрацией и поля с логином и паролем
        self.line_log_reg = [self.ui.login_line, self.ui.password_line]
        self.ui.sign_in_btn.clicked.connect(self.auth)
        self.ui.sign_up_btn.clicked.connect(self.reg)

    def hide_menu_buttons(self):
        self.ui.date_btn.hide()
        self.ui.charts_btn.hide()
        self.ui.settings_btn.hide()
        
    def show_memu_buttons(self):
        self.ui.date_btn.show()
        self.ui.charts_btn.show()
        self.ui.settings_btn.show()

    # проверка пароля
    def check_loggin_pass(funct):
        def wrapper(self):
            for line_edit in self.line_log_reg:
                if len(line_edit.text()) == 0:
                    QMessageBox.warning(self, "Ошибка", "Все поля должны быть заполнены!")
                    return
                funct(self)
        return wrapper

    # обработчик сигналов
    def signal_handler(self, value):
        if value == "Успешная авторизация":
            self.show_memu_buttons()
            self.showData()
        QMessageBox.about(self, 'Оповещение', value)

    @check_loggin_pass
    def auth(self):
        user_login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        self.check_db.thr_login(user_login, password)

    @check_loggin_pass
    def reg(self):
        user_login = self.ui.login_line.text()
        password = self.ui.password_line.text()
        self.check_db.thr_register(user_login, password)
        
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