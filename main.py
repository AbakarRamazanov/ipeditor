#!/usr/bin/python3
import sys
import os
import argparse
import json

from PySide2.QtWidgets import QApplication, QMainWindow, QLabel
from PySide2.QtWidgets import (QHBoxLayout, QHeaderView, QSizePolicy,QTableView, QWidget,QStyledItemDelegate, QHeaderView, QAbstractItemView)
from PySide2.QtCore import QFile, SIGNAL, QObject, QDateTime, QTimeZone
from ui_mainwindow import Ui_MainWindow
from DataTableModel import DataTableModel
from TableItemDelegate import TableItemDelegate


class MainWindow(QMainWindow):

    def __init__(self, data):
        QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        QObject.connect(self.ui.activateButton, SIGNAL('clicked()'), self.onClickActiveButton)
        QObject.connect(self.ui.deactivateButton, SIGNAL('clicked()'), self.onClickDeactiveButton)
        QObject.connect(self.ui.addButton, SIGNAL('clicked()'), self.onClickAddButton)
        QObject.connect(self.ui.editButton, SIGNAL('clicked()'), self.onClickEditButton)
        QObject.connect(self.ui.deleteButton, SIGNAL('clicked()'), self.onClickDeleteButton)


        self.model = DataTableModel(data)
        self.ui.table_view.setModel(self.model)
        self.ui.table_view.setItemDelegate(TableItemDelegate())

        self.ui.table_view.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)


        self.setFixedSize(self.size())
        print(self.size())

#        print(self.ui.table_view.editTriggers())
#        self.ui.table_view.setEditTriggers(QTableView.EditTrigger.DoubleClicked)



    def onClickActiveButton(self):
        print("XEP кнопка активации")
        pass

    def onClickDeactiveButton(self):
        print("XEP кнопка деактивации")
        pass

    def onClickAddButton(self):
        print("ХЕР кнопка добавления")
        pass

    def onClickEditButton(self):
        print("ХЕР кнопка изменения")
        pass

    def onClickDeleteButton(self):
        print("ХЕР кнопка удаления")
        pass




if __name__ == "__main__":
    options = argparse.ArgumentParser()
    options.add_argument("-c", "--config", type=str, required=True)
    args = options.parse_args()
    with open(args.config) as f:
        d = json.load(f)
    app = QApplication()
    window = MainWindow(d)
    window.show()
    sys.exit(app.exec_())
