from PyQt6.QtWidgets import QFileDialog, QLabel
import pandas as pd


class LoadingFile:
    def __init__(self, parent_window, status_label=None):
        self.parent = parent_window
        self.status_label = status_label
        self.df = None

    def load_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self.parent,
            "Выбирите файл",
            "",
            "CSV (*.csv);;Excel (*.xlsx *.xls);;Все файлы (*)",
        )
        
        if not file_path:
            if self.status_label:
                self.status_label.setText("Файл не выбран")
            return False, "Файл не выбран"

        try:
            if file_path.endswith(".csv"):
                self.df = pd.read_csv(file_path)
            elif file_path.endswith(".xlsx", ".xls"):
                self.df = pd.read_excel(file_path)
            else:
                if self.status_label:
                    self.status_label.setText("Неподдерживаемый формат")
                return False, "Формат файла не поддерживается"
            
            if self.status_label:
                file_name = file_path.split("/")[-1]
                self.status_label.setText(f"Загружен: {file_name}")
                return True, file_name

        except Exception as e:
            if self.status_label.setText(f"Ошибка: {str(e)}"):
                return False, f"Ошибка: {str(e)}"