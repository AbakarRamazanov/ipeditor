# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui',
# licensing of 'mainwindow.ui' applies.
#
# Created: Mon Aug  5 13:21:51 2019
#      by: pyside2-uic  running on PySide2 5.13.0
#
# WARNING! All changes made in this file will be lost!

from PySide2 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.setEnabled(True)
        MainWindow.resize(640, 480)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.table_view = QtWidgets.QTableView(self.centralwidget)
        self.table_view.setMouseTracking(False)
        self.table_view.setEditTriggers(QtWidgets.QAbstractItemView.AllEditTriggers)
        self.table_view.setDragEnabled(False)
        self.table_view.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.table_view.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.table_view.setObjectName("table_view")
        self.verticalLayout.addWidget(self.table_view)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.addButton = QtWidgets.QPushButton(self.centralwidget)
        self.addButton.setObjectName("addButton")
        self.horizontalLayout.addWidget(self.addButton)
        self.editButton = QtWidgets.QPushButton(self.centralwidget)
        self.editButton.setObjectName("editButton")
        self.horizontalLayout.addWidget(self.editButton)
        self.deleteButton = QtWidgets.QPushButton(self.centralwidget)
        self.deleteButton.setObjectName("deleteButton")
        self.horizontalLayout.addWidget(self.deleteButton)
        self.activateButton = QtWidgets.QPushButton(self.centralwidget)
        self.activateButton.setObjectName("activateButton")
        self.horizontalLayout.addWidget(self.activateButton)
        self.deactivateButton = QtWidgets.QPushButton(self.centralwidget)
        self.deactivateButton.setObjectName("deactivateButton")
        self.horizontalLayout.addWidget(self.deactivateButton)
        self.verticalLayout.addLayout(self.horizontalLayout)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 640, 22))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.action = QtWidgets.QAction(MainWindow)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(MainWindow)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(MainWindow)
        self.action_3.setObjectName("action_3")
        self.action_5 = QtWidgets.QAction(MainWindow)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(MainWindow)
        self.action_6.setObjectName("action_6")
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_5)
        self.menu_2.addAction(self.action_6)
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtWidgets.QApplication.translate("MainWindow", "MainWindow", None, -1))
        self.addButton.setText(QtWidgets.QApplication.translate("MainWindow", "Добавить", None, -1))
        self.editButton.setText(QtWidgets.QApplication.translate("MainWindow", "Изменить", None, -1))
        self.deleteButton.setText(QtWidgets.QApplication.translate("MainWindow", "Удалить", None, -1))
        self.activateButton.setText(QtWidgets.QApplication.translate("MainWindow", "Активировать выбранные", None, -1))
        self.deactivateButton.setText(QtWidgets.QApplication.translate("MainWindow", "Деактивировать выбранные", None, -1))
        self.menu.setTitle(QtWidgets.QApplication.translate("MainWindow", "Файл", None, -1))
        self.menu_2.setTitle(QtWidgets.QApplication.translate("MainWindow", "Справка", None, -1))
        self.action.setText(QtWidgets.QApplication.translate("MainWindow", "Сохранить", None, -1))
        self.action_2.setText(QtWidgets.QApplication.translate("MainWindow", "Загрузить", None, -1))
        self.action_3.setText(QtWidgets.QApplication.translate("MainWindow", "Выход", None, -1))
        self.action_5.setText(QtWidgets.QApplication.translate("MainWindow", "Выход", None, -1))
        self.action_6.setText(QtWidgets.QApplication.translate("MainWindow", "О программе", None, -1))

