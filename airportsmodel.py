 #!/usr/bin/python
 # -*- coding: utf-8 -*-

## This file is part of ISS.

## ISS is free software: you can redistribute it and/or modify
## it under the terms of the GNU General Public License as published by
## the Free Software Foundation, either version 3 of the License, or
## (at your option) any later version.

## ISS is distributed in the hope that it will be useful,
## but WITHOUT ANY WARRANTY; without even the implied warranty of
## MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
## GNU General Public License for more details.

## You should have received a copy of the GNU General Public License
## along with ISS.  If not, see <http://www.gnu.org/licenses/>.


from PyQt5.QtCore import *
from PyQt5.QtWidgets import *


class AirportsModelSort(QSortFilterProxyModel):
    """Sort model for allergens table"""

    def __init__(self, sourcemodel, parent=None):
        QSortFilterProxyModel.__init__(self,  parent)
        self.setSortCaseSensitivity(Qt.CaseInsensitive)
        self.setSourceModel(sourcemodel)


class AirportsModel(QAbstractTableModel):
    """Model for allergens table"""

    def __init__(self, parent=None):
        QAbstractTableModel.__init__(self,  parent)
        self.headerdata = [self.tr('Airport code')]
        self.modeldata = []

    def data(self, index, role):
        if not index.isValid():
            return QVariant()
        if role == Qt.DisplayRole:
            return QVariant(self.modeldata[index.row()][0])
        elif role == Qt.CheckStateRole:
            if self.modeldata[index.row()][1] == 0:
                return QVariant(Qt.Unchecked)
            else:
                return QVariant(Qt.Checked)
        return QVariant()

    def headerData(self, col, orientation, role):
        if (orientation == Qt.Horizontal) and (role == Qt.DisplayRole):
            return QVariant(self.headerdata[col])
        else:
            return QVariant()

    def setData(self, index, value, role):
        if role == Qt.CheckStateRole:
            if index.column() == 0:
                if value == Qt.Checked:
                    self.modeldata[index.row()][1] = 1
                elif value == Qt.Unchecked:
                    self.modeldata[index.row()][1] = 0
                return True
        return False

    def rowCount(self, parent=QModelIndex()):
        return len(self.modeldata)

    def columnCount(self, parent=QModelIndex()):
        return len(self.headerdata)

    def flags(self, index):
        if index.column() == 0:
            return Qt.ItemIsUserCheckable | Qt.ItemIsEnabled | Qt.ItemIsSelectable
        return Qt.ItemIsEnabled | Qt.ItemIsSelectable

    def clear(self):
        """Clears all data"""
        self.beginResetModel()
        self.modeldata = []
        self.endResetModel()
        
    def loadData(self, data):
        """Loads data to internal structure"""
        self.beginResetModel()
        data = eval(data)
        new_data = []
        for label in data:
            new_data.append([label, 1])
        self.modeldata = new_data
        self.endResetModel()

    def getCheckedItems(self):
        new_data = []
        for data in self.modeldata:
            if data[1] == 1:
                new_data.append(data[0])
        return new_data

# End of airportsmodel.py
