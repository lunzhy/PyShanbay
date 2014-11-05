#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from PyQt4.QtCore import *


class MainFormWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()
        self.set_ui_text()
        self.set_widget_property()

        self.tb_members_data = []

    def setup_ui(self):
        # to do with the main form
        self.resize(558, 512)

        # vertical layout users
        self.verticalLayoutWidget = QtGui.QWidget(self)
        self.verticalLayoutWidget.setGeometry(QtCore.QRect(9, 9, 241, 491))
        self.verticalLayout_users = QtGui.QVBoxLayout(self.verticalLayoutWidget)
        self.verticalLayout_users.setMargin(0)
        self.table_members = QtGui.QTableWidget(self.verticalLayoutWidget)
        self.table_members.setColumnCount(0)
        self.table_members.setRowCount(0)
        self.verticalLayout_users.addWidget(self.table_members)
        self.horizontalLayout_refresh = QtGui.QHBoxLayout()
        self.btn_refresh = QtGui.QPushButton(self.verticalLayoutWidget)
        self.horizontalLayout_refresh.addWidget(self.btn_refresh)
        self.label_refresh_time = QtGui.QLabel(self.verticalLayoutWidget)
        self.horizontalLayout_refresh.addWidget(self.label_refresh_time)
        self.verticalLayout_users.addLayout(self.horizontalLayout_refresh)
        # end vertical layout users

        # line separator
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(260, 90, 281, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3 = QtGui.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(260, 240, 281, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)

        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(260, 260, 277, 128))
        self.gridLayout_recentCheckin = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_recentCheckin.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentCheckin.setMargin(0)

        self.tb_recent_checkin = QtGui.QTableWidget(self.layoutWidget)
        self.tb_recent_checkin.setColumnCount(0)
        self.tb_recent_checkin.setRowCount(0)
        self.gridLayout_recentCheckin.addWidget(self.tb_recent_checkin, 1, 0, 1, 3)
        self.label_recent_checkin = QtGui.QLabel(self.layoutWidget)
        self.gridLayout_recentCheckin.addWidget(self.label_recent_checkin, 0, 0, 1, 1)
        self.btn_recent_checkin = QtGui.QPushButton(self.layoutWidget)

        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_checkin.sizePolicy().hasHeightForWidth())
        self.btn_recent_checkin.setSizePolicy(sizePolicy)

        self.gridLayout_recentCheckin.addWidget(self.btn_recent_checkin, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentCheckin.addItem(spacerItem, 0, 1, 1, 1)
        self.line_4 = QtGui.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(260, 390, 281, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)

        self.layoutWidget1 = QtGui.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(260, 410, 281, 102))
        self.gridLayout_kickout = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_kickout.setMargin(0)
        self.textEdit_msg = QtGui.QPlainTextEdit(self.layoutWidget1)
        self.gridLayout_kickout.addWidget(self.textEdit_msg, 1, 0, 1, 3)
        self.chb_message = QtGui.QCheckBox(self.layoutWidget1)
        self.gridLayout_kickout.addWidget(self.chb_message, 0, 2, 1, 1)
        self.btn_kickout = QtGui.QPushButton(self.layoutWidget1)
        self.gridLayout_kickout.addWidget(self.btn_kickout, 0, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_kickout.addItem(spacerItem1, 0, 1, 1, 1)

        self.layoutWidget2 = QtGui.QWidget(self)
        self.layoutWidget2.setGeometry(QtCore.QRect(260, 10, 278, 81))
        self.gridLayout_userinfo = QtGui.QGridLayout(self.layoutWidget2)
        self.gridLayout_userinfo.setSizeConstraint(QtGui.QLayout.SetDefaultConstraint)
        self.gridLayout_userinfo.setMargin(0)
        self.text_points = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_points, 2, 1, 1, 2)
        self.text_checkin = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_checkin, 0, 4, 1, 2)
        self.text_nickname = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_nickname, 0, 1, 1, 2)
        self.label_days = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_days, 1, 0, 1, 1)
        self.text_rank = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_rank, 1, 4, 1, 2)
        self.label_nickname = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_nickname, 0, 0, 1, 1)
        self.label_checkin = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_checkin, 0, 3, 1, 1)
        self.text_days = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_days, 1, 1, 1, 2)
        self.label_points = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_points, 2, 0, 1, 1)
        self.label_rank = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_rank, 1, 3, 1, 1)
        self.label_rate = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.label_rate, 2, 3, 1, 1)
        self.text_rates = QtGui.QLabel(self.layoutWidget2)
        self.gridLayout_userinfo.addWidget(self.text_rates, 2, 4, 1, 2)

        self.layoutWidget3 = QtGui.QWidget(self)
        self.layoutWidget3.setGeometry(QtCore.QRect(260, 110, 277, 128))
        self.gridLayout_recentWord = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout_recentWord.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentWord.setMargin(0)
        self.label_recent_words = QtGui.QLabel(self.layoutWidget3)
        self.gridLayout_recentWord.addWidget(self.label_recent_words, 0, 0, 1, 1)
        self.btn_recent_words = QtGui.QPushButton(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_words.sizePolicy().hasHeightForWidth())
        self.btn_recent_words.setSizePolicy(sizePolicy)
        self.gridLayout_recentWord.addWidget(self.btn_recent_words, 0, 2, 1, 1)

        spacerItem2 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentWord.addItem(spacerItem2, 0, 1, 1, 1)
        self.tb_recent_words = QtGui.QTableWidget(self.layoutWidget3)
        self.tb_recent_words.setColumnCount(0)
        self.tb_recent_words.setRowCount(0)
        self.gridLayout_recentWord.addWidget(self.tb_recent_words, 1, 0, 1, 3)

        return

    def set_ui_text(self):
        self.setWindowTitle("Shanbay Manage")
        self.btn_refresh.setText("刷新")
        self.label_refresh_time.setText("TextLabel")
        self.label_recent_checkin.setText("最近七天打卡情况")
        self.btn_recent_checkin.setText("获取")
        self.chb_message.setText("发送短信")
        self.btn_kickout.setText("踢出小组")
        self.text_points.setText("TextLabel")
        self.text_checkin.setText("TextLabel")
        self.text_nickname.setText("TextLabel")
        self.text_rank.setText("TextLabel")
        self.text_days.setText("TextLabel")
        self.text_rates.setText("TextLabel")
        self.label_days.setText("组龄：")
        self.label_nickname.setText("昵称：")
        self.label_checkin.setText("打卡：")
        self.label_points.setText("成长值：")
        self.label_rank.setText("排名：")
        self.label_rate.setText("打卡率：")
        self.label_recent_words.setText("最近七天背词情况")
        self.btn_recent_words.setText("获取")
        return

    def set_widget_property(self):
        self.table_members.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.table_members.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.table_members.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.table_members.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)

        self.table_members.itemClicked.connect(self.selected_member)
        # self.btn_refresh.clicked.connect(lambda: self.set_data_members([]))
        return

    def set_data_members(self, members_data):
        self.tb_members_data = members_data

        self.table_members.setColumnCount(2)
        self.table_members.setRowCount(len(members_data))

        for row_index, member in enumerate(members_data):
            new_item = QtGui.QTableWidgetItem(member['nickname'])
            self.table_members.setItem(row_index, 0, new_item)
            new_item = QtGui.QTableWidgetItem(str(member['checked_today']))
            self.table_members.setItem(row_index, 1, new_item)
        return

    def selected_member(self):
        select = self.table_members.selectionModel().selectedRows()
        row = select[0].row()
        member = self.tb_members_data[row]
        self.text_nickname.setText(member['nickname'])
        self.text_checkin.setText('已打卡' if member['checked_today'] else '未打卡')
        self.text_days.setText(member['days'])
        self.text_rank.setText(str(row+1))
        self.text_points.setText(member['points'])
        self.text_rates.setText(member['rate'])
        return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MainFormWidget()

    main_form.show()
    app.exec_()