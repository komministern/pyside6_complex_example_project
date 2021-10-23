"""
Copyright (C) 2021 Oscar Franzén <oscarfranzen@protonmail.com>

This file is part of PySide6 Complex Example Project.

PySide6 Complex Example Project is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

PySide6 Complex Example Project is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with PySide6 Complex Example Project.  If not, see <https://www.gnu.org/licenses/>.
"""

from PySide6 import QtCore, QtGui, QtWidgets


class MyCalendarWidget(QtWidgets.QCalendarWidget):
    def __init__(self, parent=None):
        super(MyCalendarWidget, self).__init__(parent)
        # QtWidgets.QCalendarWidget.__init__(self, parent)
        
        self.setFirstDayOfWeek(QtCore.Qt.DayOfWeek.Monday)

        self.setGreenDates([])

        self.light_green = QtGui.QColor.fromRgbF(0.75,1.00,0.70)

    def setGreenDates(self, list_of_dates):
        self.green_dates = list_of_dates

    def paintCell(self, painter, rect, date):
        painter.setRenderHint(QtGui.QPainter.Antialiasing)

        if date in self.green_dates:
            painter.fillRect(rect, self.light_green)
        else:
            painter.fillRect(rect, QtGui.QColor('white'))
        
        painter.drawText(rect, QtCore.Qt.AlignCenter, str(date.day()))

        if date == self.selectedDate():
            newUpperLeft = QtCore.QPoint(rect.topLeft().x() + 1, rect.topLeft().y() + 1)
            newBottomRight = QtCore.QPoint(rect.bottomRight().x() - 1, rect.bottomRight().y() - 1)
            new_rect = QtCore.QRect(newUpperLeft, newBottomRight)

            painter.drawEllipse(new_rect)




