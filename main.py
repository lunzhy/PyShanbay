#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from pyshanbay.main_widget import MainWidget
from pyshanbay.config import ShanbayConfig


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    config = ShanbayConfig()
    main_form = MainWidget(config)
    main_form.show()
    app.exec_()