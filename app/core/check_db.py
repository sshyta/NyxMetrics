from PyQt6 import QtCore, QtGui, QtWidgets
from app.core.handler.db_handler import *

class CheckThread(QtCore.QThread):
    mysignal = QtCore.pyqtSignal(str)

    def thr_login(self, user_login, password):
        login(user_login, password, self.mysignal)
    
    def thr_register(self, user_login, password):
        register(user_login, password, self.mysignal)