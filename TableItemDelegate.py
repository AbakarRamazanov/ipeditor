# This Python file uses the following encoding: utf-8
from PySide2 import QtCore
from PySide2 import QtWidgets
from PySide2.QtWidgets import (QStyledItemDelegate, QTextEdit)

class TableItemDelegate(QStyledItemDelegate):
    def __init__(self, parent=None):
        super(TableItemDelegate, self).__init__(parent)
        pass

    def createEditor(parent, option, index):
        print("XEP createEditor")
        qte = QTextEdit(parent)
        qte.setText("XEP qte")
        return qte
        pass

    def setEditorData(editor, index):
        pass

    def setModelData(editor, model, index):
        pass

    def commitAndCloseEditor():
        pass


