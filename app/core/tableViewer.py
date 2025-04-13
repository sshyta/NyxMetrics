from PyQt6.QtWidgets import QTableView, QHeaderView
from PyQt6.QtGui import QStandardItemModel, QStandardItem


class TableViewer(QTableView):
    def __init__(self):
        super().__init__()
        self.__setup_table()
    
        
    def __setup_table(self):
        self.setAlternatingRowColors(True)
        self.horizontalHeader().setSelectionResizeMode(QHeaderView.Stretch)
        self.setModel(QStandardItemModel())
        
    
    def display_data(self, data):
        model = QStandardItemModel()
        
        if not data.empty:
            model.setHorizontalHeaderLabels(data.columns.astype(str))
            
            for _, row in data.iterrows():
                items = [QStandardItem(str(val)) for val in row]
                model.appendRow(items)
            
        self.setModel(model)
        self.resizeColumnsToContents()        