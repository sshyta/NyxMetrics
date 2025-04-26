# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PyQt6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PyQt6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PyQt6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QStackedWidget, QTableView, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1101, 750)
        MainWindow.setStyleSheet(u"background-color: #424242;\n"
"font-family: Zen Kaku Gothic New;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 50, 1091, 671))
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.stackedWidget.addWidget(self.Home)
        self.Data = QWidget()
        self.Data.setObjectName(u"Data")
        self.tableView = QTableView(self.Data)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 60, 1071, 601))
        self.layoutWidget = QWidget(self.Data)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 30, 361, 27))
        self.gridLayout = QGridLayout(self.layoutWidget)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = QPushButton(self.layoutWidget)
        self.uploadButton.setObjectName(u"uploadButton")

        self.gridLayout.addWidget(self.uploadButton, 0, 0, 1, 1)

        self.status_label = QLabel(self.layoutWidget)
        self.status_label.setObjectName(u"status_label")

        self.gridLayout.addWidget(self.status_label, 0, 1, 1, 1)

        self.clearButton = QPushButton(self.layoutWidget)
        self.clearButton.setObjectName(u"clearButton")

        self.gridLayout.addWidget(self.clearButton, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.Data)
        self.Charts = QWidget()
        self.Charts.setObjectName(u"Charts")
        self.stackedWidget.addWidget(self.Charts)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.stackedWidget.addWidget(self.Settings)
        self.layoutWidget1 = QWidget(self.centralwidget)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(20, 10, 340, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.layoutWidget1)
        self.home_btn.setObjectName(u"home_btn")

        self.horizontalLayout.addWidget(self.home_btn)

        self.date_btn = QPushButton(self.layoutWidget1)
        self.date_btn.setObjectName(u"date_btn")

        self.horizontalLayout.addWidget(self.date_btn)

        self.charts_btn = QPushButton(self.layoutWidget1)
        self.charts_btn.setObjectName(u"charts_btn")

        self.horizontalLayout.addWidget(self.charts_btn)

        self.settings_btn = QPushButton(self.layoutWidget1)
        self.settings_btn.setObjectName(u"settings_btn")

        self.horizontalLayout.addWidget(self.settings_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nyx metrics", None))
        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload file...", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u0421lear", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.date_btn.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.charts_btn.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi