# This Python file uses the following encoding: utf-8

import json

from PySide2.QtCore import Qt, QAbstractTableModel, QModelIndex
from PySide2 import QtWidgets
from PySide2.QtGui import QColor

class DataTableModel(QAbstractTableModel):

    class Ip():

        def __init__(self, ip, gateway, turn_on):
            self.ip = ip
            self.gateway = gateway
            self.turn_on = turn_on
            pass

    def load_data(self, data):
        self.ips = []
        for d in data:
            self.ips.append(self.Ip(d["ip"],d["gateway"],d["turn_on"]))
        for ip in self.ips:
            print("ip = " + str(ip.ip) + "; gateway = " + str(ip.gateway) + "; turn_on = " + str(ip.turn_on))
#        self.input_dates = data[0].values
#        self.input_magnitudes = data[1].values

        self.column_count = 3
        self.row_count = len(self.ips)

    def rowCount(self, parent=QModelIndex()):
        return len(self.ips)

    def columnCount(self, parent=QModelIndex()):
        return 3

    def headerData(self, section, orientation, role):
        if role != Qt.DisplayRole:
            return None
        if orientation == Qt.Horizontal:
            return ("Ip", "Gateway", "Turn on")[section]
        else:
            return "{}".format(section)

    def data(self, index, role=Qt.DisplayRole):
        column = index.column()
        row = index.row()
        ip = self.ips[row]

        if role == Qt.DisplayRole:
            if column == 0:
                return ip.ip
            elif column == 1:
                return ip.gateway
            elif column == 2:
                return ip.turn_on
        elif role == Qt.BackgroundRole:
            return QColor(Qt.white)
        elif role == Qt.TextAlignmentRole:
            return Qt.AlignRight

        return None

    def __init__(self, data=None):
            QAbstractTableModel.__init__(self)
            self.load_data(data)


