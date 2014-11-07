#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from PyQt4 import QtGui
from PyQt4 import QtCore


class ParseException(Exception):
    pass


class ShanbayConnectException(Exception):
    pass


def clickable(widget):
    class Filter(QtCore.QObject):

        clicked = QtCore.pyqtSignal()

        def eventFilter(self, obj, event):
            if obj == widget:
                if event.type() == QtCore.QEvent.MouseButtonRelease:
                    if obj.rect().contains(event.pos()):
                        self.clicked.emit()
                    # The developer can opt for .emit(obj) to get the object within the slot.
                    return True
            return False

    filter = Filter(widget)
    widget.installEventFilter(filter)
    return filter.clicked