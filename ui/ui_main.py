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
    QLabel, QLineEdit, QMainWindow, QPushButton,
    QSizePolicy, QStackedWidget, QTableView, QVBoxLayout, QWidget, QFrame)


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
        self.layoutWidget = QWidget(self.Home)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(830, 282, 171, 61))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.login_line = QLineEdit(self.layoutWidget)
        self.login_line.setObjectName(u"login_line")

        self.verticalLayout.addWidget(self.login_line)

        self.password_line = QLineEdit(self.layoutWidget)
        self.password_line.setObjectName(u"password_line")

        self.verticalLayout.addWidget(self.password_line)

        self.layoutWidget1 = QWidget(self.Home)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(830, 350, 171, 27))
        self.horizontalLayout_2 = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.sign_in_btn = QPushButton(self.layoutWidget1)
        self.sign_in_btn.setObjectName(u"sign_in_btn")

        self.horizontalLayout_2.addWidget(self.sign_in_btn)

        self.sign_up_btn = QPushButton(self.layoutWidget1)
        self.sign_up_btn.setObjectName(u"sign_up_btn")

        self.horizontalLayout_2.addWidget(self.sign_up_btn)

        self.stackedWidget.addWidget(self.Home)
        self.Data = QWidget()
        self.Data.setObjectName(u"Data")
        self.tableView = QTableView(self.Data)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(20, 60, 1071, 601))
        self.layoutWidget2 = QWidget(self.Data)
        self.layoutWidget2.setObjectName(u"layoutWidget2")
        self.layoutWidget2.setGeometry(QRect(20, 30, 361, 27))
        self.gridLayout = QGridLayout(self.layoutWidget2)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.uploadButton = QPushButton(self.layoutWidget2)
        self.uploadButton.setObjectName(u"uploadButton")

        self.gridLayout.addWidget(self.uploadButton, 0, 0, 1, 1)

        self.status_label = QLabel(self.layoutWidget2)
        self.status_label.setObjectName(u"status_label")

        self.gridLayout.addWidget(self.status_label, 0, 1, 1, 1)

        self.clearButton = QPushButton(self.layoutWidget2)
        self.clearButton.setObjectName(u"clearButton")

        self.gridLayout.addWidget(self.clearButton, 0, 2, 1, 1)

        self.stackedWidget.addWidget(self.Data)
        self.Charts = QWidget()
        self.Charts.setObjectName(u"Charts")
        self.graph_container = QFrame(self.Charts)
        self.graph_container.setObjectName(u"graph_container")
        self.graph_container.setGeometry(QRect(270, 60, 821, 601))
        self.graph_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.graph_container.setFrameShadow(QFrame.Shadow.Raised)
        self.preset_container = QFrame(self.Charts)
        self.preset_container.setObjectName(u"preset_container")
        self.preset_container.setGeometry(QRect(20, 60, 241, 601))
        self.preset_container.setFrameShape(QFrame.Shape.StyledPanel)
        self.preset_container.setFrameShadow(QFrame.Shadow.Raised)
        self.stackedWidget.addWidget(self.Charts)
        self.Settings = QWidget()
        self.Settings.setObjectName(u"Settings")
        self.stackedWidget.addWidget(self.Settings)
        self.layoutWidget3 = QWidget(self.centralwidget)
        self.layoutWidget3.setObjectName(u"layoutWidget3")
        self.layoutWidget3.setGeometry(QRect(20, 10, 340, 27))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget3)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.home_btn = QPushButton(self.layoutWidget3)
        self.home_btn.setObjectName(u"home_btn")

        self.horizontalLayout.addWidget(self.home_btn)

        self.date_btn = QPushButton(self.layoutWidget3)
        self.date_btn.setObjectName(u"date_btn")

        self.horizontalLayout.addWidget(self.date_btn)

        self.charts_btn = QPushButton(self.layoutWidget3)
        self.charts_btn.setObjectName(u"charts_btn")

        self.horizontalLayout.addWidget(self.charts_btn)


        self.settings_btn = QPushButton(self.layoutWidget1)
        self.settings_btn.setObjectName(u"settings_btn")

        self.horizontalLayout.addWidget(self.settings_btn)

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


        self.settings_btn = QPushButton(self.layoutWidget3)
        self.settings_btn.setObjectName(u"settings_btn")

        self.horizontalLayout.addWidget(self.settings_btn)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)


        self.stackedWidget.setCurrentIndex(0)



        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"Nyx metrics", None))


        self.login_line.setText("")
        self.login_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Login...", None))
        self.password_line.setText("")
        self.password_line.setPlaceholderText(QCoreApplication.translate("MainWindow", u"Password...", None))
        self.sign_in_btn.setText(QCoreApplication.translate("MainWindow", u"Sign in", None))
        self.sign_up_btn.setText(QCoreApplication.translate("MainWindow", u"Sign up", None))

        self.uploadButton.setText(QCoreApplication.translate("MainWindow", u"Upload file...", None))
        self.status_label.setText(QCoreApplication.translate("MainWindow", u"\u0424\u0430\u0439\u043b \u043d\u0435 \u0432\u044b\u0431\u0440\u0430\u043d", None))
        self.clearButton.setText(QCoreApplication.translate("MainWindow", u"\u0421lear", None))
        self.home_btn.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.date_btn.setText(QCoreApplication.translate("MainWindow", u"Data", None))
        self.
        _btn.setText(QCoreApplication.translate("MainWindow", u"Charts", None))
        self.settings_btn.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
    # retranslateUi