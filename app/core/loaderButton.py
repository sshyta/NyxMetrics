from PyQt6.QtWidgets import QFileDialog

class LoadingFile:
    def __init__(self, parent_window):
        self.parent = parent_window
        
    def load_file(self):
        print('кнопка нажата') 
        
        ########### Логика для загрузки файла
        