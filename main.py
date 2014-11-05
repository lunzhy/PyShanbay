#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from pyshanbay.main_widget import MainWidget


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MainWidget()
    main_form.show()
    app.exec_()