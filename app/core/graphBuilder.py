import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QVBoxLayout, QFrame
from ui.ui_main import Ui_MainWindow
from app.core.loaderButton import LoadingFile
from app.core.tableViewer import TableViewer
from matplotlib.backends.backend_qtagg import FigureCanvas
from matplotlib.backends.backend_qtagg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg
from matplotlib.figure import Figure

class MplCanvas(FigureCanvasQTAgg):
    def __init__ (self, parent=None, width = 5, height = 4, dpi = 100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)