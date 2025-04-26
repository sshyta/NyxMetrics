from PyQt6.QtWidgets import QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class TableViewer(QTableView):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.__setup_table()
        

    def __setup_table(self):
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        self.setModel(QStandardItemModel())
        
    
    def display_data(self, data):
        model = QStandardItemModel() # Создание новой модели данных
        
        if not data.empty:
            model.setHorizontalHeaderLabels(data.columns.astype(str)) # Парсим заголовки из дата сета
            
            for _, row in data.iterrows():
                items = [QStandardItem(str(val)) for val in row]
                model.appendRow(items)
            
        self.setModel(model)
        self.resizeColumnsToContents() 

    def clear_data(self):
        self.setModel(QStandardItemModel())   