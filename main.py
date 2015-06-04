#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from pyshanbay.main_widget import MainWidget
from pyshanbay.config import ShanbayConfig, DebugLog
from pyshanbay.utils import *
import ctypes


if __name__ == '__main__':

    myappid = 'ShanbayTeam.Helper'  # arbitrary string
    ctypes.windll.shell32.SetCurrentProcessExplicitAppUserModelID(myappid)

    app = QtGui.QApplication(sys.argv)
    config = ShanbayConfig()
    debug_log = DebugLog()
    try:
        main_form = MainWidget(config, debug_log)
        main_form.show()
        app.setWindowIcon(QtGui.QIcon('icon.ico'))
        app.exec_()
    except ShanbayConnectException:
        msg = 'Login Error !\n\nPlease check your username and password in config.ini file.\n' \
              'If this error occurs again, please log in Shanbay.com on the web first.'
        QtGui.QMessageBox.warning(None, 'Error', msg,
                                        QtGui.QMessageBox.Ok,
                                        QtGui.QMessageBox.Ok)
        app.exit()