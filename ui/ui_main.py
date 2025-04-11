# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (
    QCoreApplication,
    QDate,
    QDateTime,
    QLocale,
    QMetaObject,
    QObject,
    QPoint,
    QRect,
    QSize,
    QTime,
    QUrl,
    Qt,
)
from PyQt6.QtGui import (
    QAction,
    QBrush,
    QColor,
    QConicalGradient,
    QCursor,
    QFont,
    QFontDatabase,
    QGradient,
    QIcon,
    QImage,
    QKeySequence,
    QLinearGradient,
    QPainter,
    QPalette,
    QPixmap,
    QRadialGradient,
    QTransform,
)
from PyQt6.QtWidgets import (
    QApplication,
    QGridLayout,
    QHeaderView,
    QLabel,
    QMainWindow,
    QMenu,
    QMenuBar,
    QPushButton,
    QSizePolicy,
    QStatusBar,
    QTableView,
    QWidget,
)



class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1115, 750)
        MainWindow.setStyleSheet(
            "background-color: #424242;\n" "font-family: Zen Kaku Gothic New;"
        )
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableView = QTableView(self.centralwidget)
        self.tableView.setObjectName("tableView")
        self.tableView.setGeometry(QRect(20, 70, 1071, 611))
        self.layoutWidget = QWidget(self.centralwidget)
        self.layoutWidget.setObjectName("layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 361, 27))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName("pushButton")

        self.gridLayout.addWidget(self.pushButton, 0, 0, 1, 1)

        self.status_label = QLabel(self.layoutWidget)
        self.status_label.setObjectName("status_label")

        self.gridLayout.addWidget(self.status_label, 0, 1, 1, 1)

        self.pushButton_2 = QPushButton(self.layoutWidget)
        self.pushButton_2.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.pushButton_2, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName("menubar")
        self.menubar.setGeometry(QRect(0, 0, 1115, 33))
        self.menubar.setDefaultUp(False)
        self.menubar.setNativeMenuBar(False)
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu.setToolTipsVisible(True)
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menuData = QMenu(self.menubar)
        self.menuData.setObjectName("menuData")
        self.menuSettings = QMenu(self.menubar)
        self.menuSettings.setObjectName("menuSettings")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menuData.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menuSettings.menuAction())

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi
    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "Nyx metrics", None)
        )
        self.pushButton.setText(
            QCoreApplication.translate("MainWindow", "Upload file...", None)
        )
        self.status_label.setText(
            QCoreApplication.translate(
                "MainWindow",
                "\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d",
                None,
            )
        )
        self.pushButton_2.setText(
            QCoreApplication.translate("MainWindow", "\u0421lear", None)
        )
        self.menu.setTitle(QCoreApplication.translate("MainWindow", "Home", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", "Charts", None))
        self.menuData.setTitle(QCoreApplication.translate("MainWindow", "Data", None))
        self.menuSettings.setTitle(
            QCoreApplication.translate("MainWindow", "Settings", None)
        )
    # retranslateUi