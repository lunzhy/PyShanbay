#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from PyQt4 import QtGui
from PyQt4 import QtCore


try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s


class UIMainWidget(QtGui.QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName(_fromUtf8("UIMainWidget"))
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setEnabled(True)
        self.resize(814, 665)
        self.setMinimumSize(QtCore.QSize(814, 665))
        self.setMaximumSize(QtCore.QSize(814, 665))
        self.line = QtGui.QFrame(self)
        self.line.setGeometry(QtCore.QRect(470, 130, 331, 20))
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.line_3 = QtGui.QFrame(self)
        self.line_3.setGeometry(QtCore.QRect(470, 260, 331, 20))
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.layoutWidget = QtGui.QWidget(self)
        self.layoutWidget.setGeometry(QtCore.QRect(470, 280, 331, 141))
        self.layoutWidget.setObjectName(_fromUtf8("layoutWidget"))
        self.gridLayout_recentCheckin = QtGui.QGridLayout(self.layoutWidget)
        self.gridLayout_recentCheckin.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentCheckin.setMargin(0)
        self.gridLayout_recentCheckin.setObjectName(_fromUtf8("gridLayout_recentCheckin"))
        self.label_recent_checkin = QtGui.QLabel(self.layoutWidget)
        self.label_recent_checkin.setObjectName(_fromUtf8("label_recent_checkin"))
        self.gridLayout_recentCheckin.addWidget(self.label_recent_checkin, 0, 0, 1, 1)
        self.btn_recent_checkin = QtGui.QPushButton(self.layoutWidget)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_checkin.sizePolicy().hasHeightForWidth())
        self.btn_recent_checkin.setSizePolicy(sizePolicy)
        self.btn_recent_checkin.setObjectName(_fromUtf8("btn_recent_checkin"))
        self.gridLayout_recentCheckin.addWidget(self.btn_recent_checkin, 0, 2, 1, 1)
        spacerItem = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                       QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentCheckin.addItem(spacerItem, 0, 1, 1, 1)
        self.tb_recent_checkin = QtGui.QTableWidget(self.layoutWidget)
        self.tb_recent_checkin.setObjectName(_fromUtf8("tb_recent_checkin"))
        self.tb_recent_checkin.setColumnCount(0)
        self.tb_recent_checkin.setRowCount(0)
        self.gridLayout_recentCheckin.addWidget(self.tb_recent_checkin, 1, 0, 1, 3)
        self.line_4 = QtGui.QFrame(self)
        self.line_4.setGeometry(QtCore.QRect(470, 420, 331, 20))
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.layoutWidget1 = QtGui.QWidget(self)
        self.layoutWidget1.setGeometry(QtCore.QRect(470, 150, 331, 111))
        self.layoutWidget1.setObjectName(_fromUtf8("layoutWidget1"))
        self.gridLayout_recentWord = QtGui.QGridLayout(self.layoutWidget1)
        self.gridLayout_recentWord.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentWord.setMargin(0)
        self.gridLayout_recentWord.setObjectName(_fromUtf8("gridLayout_recentWord"))
        self.label_recent_words = QtGui.QLabel(self.layoutWidget1)
        self.label_recent_words.setObjectName(_fromUtf8("label_recent_words"))
        self.gridLayout_recentWord.addWidget(self.label_recent_words, 0, 0, 1, 1)
        self.btn_recent_words = QtGui.QPushButton(self.layoutWidget1)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_words.sizePolicy().hasHeightForWidth())
        self.btn_recent_words.setSizePolicy(sizePolicy)
        self.btn_recent_words.setObjectName(_fromUtf8("btn_recent_words"))
        self.gridLayout_recentWord.addWidget(self.btn_recent_words, 0, 2, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentWord.addItem(spacerItem1, 0, 1, 1, 1)
        self.tb_recent_words = QtGui.QTableWidget(self.layoutWidget1)
        self.tb_recent_words.setObjectName(_fromUtf8("tb_recent_words"))
        self.tb_recent_words.setColumnCount(0)
        self.tb_recent_words.setRowCount(0)
        self.gridLayout_recentWord.addWidget(self.tb_recent_words, 1, 0, 1, 3)
        self.line_5 = QtGui.QFrame(self)
        self.line_5.setGeometry(QtCore.QRect(470, 571, 331, 20))
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.btn_refresh = QtGui.QPushButton(self)
        self.btn_refresh.setGeometry(QtCore.QRect(728, 630, 75, 23))
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.label_refresh_time = QtGui.QLabel(self)
        self.label_refresh_time.setGeometry(QtCore.QRect(10, 640, 161, 16))
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_refresh_time.sizePolicy().hasHeightForWidth())
        self.label_refresh_time.setSizePolicy(sizePolicy)
        self.label_refresh_time.setObjectName(_fromUtf8("label_refresh_time"))
        self.layoutWidget2 = QtGui.QWidget(self)
        self.layoutWidget2.setGeometry(QtCore.QRect(10, 10, 431, 611))
        self.layoutWidget2.setObjectName(_fromUtf8("layoutWidget2"))
        self.horizontalLayout = QtGui.QHBoxLayout(self.layoutWidget2)
        self.horizontalLayout.setMargin(0)
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.label_search = QtGui.QLabel(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setObjectName(_fromUtf8("label_search"))
        self.gridLayout_5.addWidget(self.label_search, 0, 0, 1, 1)
        self.tb_members = QtGui.QTableWidget(self.layoutWidget2)
        self.tb_members.setFrameShape(QtGui.QFrame.NoFrame)
        self.tb_members.setObjectName(_fromUtf8("tb_members"))
        self.tb_members.setColumnCount(0)
        self.tb_members.setRowCount(0)
        self.gridLayout_5.addWidget(self.tb_members, 1, 0, 1, 2)
        self.cbb_team_condition = QtGui.QComboBox(self.layoutWidget2)
        self.cbb_team_condition.setObjectName(_fromUtf8("cbb_team_condition"))
        self.gridLayout_5.addWidget(self.cbb_team_condition, 2, 0, 1, 2)
        self.edit_search = QtGui.QLineEdit(self.layoutWidget2)
        self.edit_search.setObjectName(_fromUtf8("edit_search"))
        self.gridLayout_5.addWidget(self.edit_search, 0, 1, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem2 = QtGui.QSpacerItem(20, 138, QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.btn_group_add = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_group_add.sizePolicy().hasHeightForWidth())
        self.btn_group_add.setSizePolicy(sizePolicy)
        self.btn_group_add.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_group_add.setObjectName(_fromUtf8("btn_group_add"))
        self.verticalLayout.addWidget(self.btn_group_add)
        spacerItem3 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem3)
        self.btn_group_remove = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_group_remove.sizePolicy().hasHeightForWidth())
        self.btn_group_remove.setSizePolicy(sizePolicy)
        self.btn_group_remove.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_group_remove.setObjectName(_fromUtf8("btn_group_remove"))
        self.verticalLayout.addWidget(self.btn_group_remove)
        spacerItem4 = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem4)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.cbb_group_list = QtGui.QComboBox(self.layoutWidget2)
        self.cbb_group_list.setObjectName(_fromUtf8("cbb_group_list"))
        self.gridLayout_4.addWidget(self.cbb_group_list, 0, 0, 1, 1)
        self.tb_group_selected = QtGui.QTableWidget(self.layoutWidget2)
        self.tb_group_selected.setObjectName(_fromUtf8("tb_group_selected"))
        self.tb_group_selected.setColumnCount(0)
        self.tb_group_selected.setRowCount(0)
        self.gridLayout_4.addWidget(self.tb_group_selected, 1, 0, 1, 1)
        self.btn_save_group = QtGui.QPushButton(self.layoutWidget2)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_group.sizePolicy().hasHeightForWidth())
        self.btn_save_group.setSizePolicy(sizePolicy)
        self.btn_save_group.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save_group.setFlat(False)
        self.btn_save_group.setObjectName(_fromUtf8("btn_save_group"))
        self.gridLayout_4.addWidget(self.btn_save_group, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.layoutWidget3 = QtGui.QWidget(self)
        self.layoutWidget3.setGeometry(QtCore.QRect(470, 20, 331, 111))
        self.layoutWidget3.setObjectName(_fromUtf8("layoutWidget3"))
        self.gridLayout = QtGui.QGridLayout(self.layoutWidget3)
        self.gridLayout.setMargin(0)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.text_checkin = QtGui.QLabel(self.layoutWidget3)
        self.text_checkin.setObjectName(_fromUtf8("text_checkin"))
        self.gridLayout.addWidget(self.text_checkin, 0, 3, 1, 1)
        self.text_points = QtGui.QLabel(self.layoutWidget3)
        self.text_points.setObjectName(_fromUtf8("text_points"))
        self.gridLayout.addWidget(self.text_points, 2, 1, 1, 1)
        self.label_nickname = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nickname.sizePolicy().hasHeightForWidth())
        self.label_nickname.setSizePolicy(sizePolicy)
        self.label_nickname.setObjectName(_fromUtf8("label_nickname"))
        self.gridLayout.addWidget(self.label_nickname, 0, 0, 1, 1)
        self.text_rates = QtGui.QLabel(self.layoutWidget3)
        self.text_rates.setObjectName(_fromUtf8("text_rates"))
        self.gridLayout.addWidget(self.text_rates, 2, 3, 1, 1)
        self.text_rank = QtGui.QLabel(self.layoutWidget3)
        self.text_rank.setObjectName(_fromUtf8("text_rank"))
        self.gridLayout.addWidget(self.text_rank, 1, 3, 1, 1)
        self.label_rank = QtGui.QLabel(self.layoutWidget3)
        self.label_rank.setObjectName(_fromUtf8("label_rank"))
        self.gridLayout.addWidget(self.label_rank, 1, 2, 1, 1)
        self.label_checkin = QtGui.QLabel(self.layoutWidget3)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_checkin.sizePolicy().hasHeightForWidth())
        self.label_checkin.setSizePolicy(sizePolicy)
        self.label_checkin.setObjectName(_fromUtf8("label_checkin"))
        self.gridLayout.addWidget(self.label_checkin, 0, 2, 1, 1)
        self.label_days = QtGui.QLabel(self.layoutWidget3)
        self.label_days.setObjectName(_fromUtf8("label_days"))
        self.gridLayout.addWidget(self.label_days, 1, 0, 1, 1)
        self.text_nickname = QtGui.QLabel(self.layoutWidget3)
        self.text_nickname.setObjectName(_fromUtf8("text_nickname"))
        self.gridLayout.addWidget(self.text_nickname, 0, 1, 1, 1)
        self.label_rate = QtGui.QLabel(self.layoutWidget3)
        self.label_rate.setObjectName(_fromUtf8("label_rate"))
        self.gridLayout.addWidget(self.label_rate, 2, 2, 1, 1)
        self.text_checkins = QtGui.QLabel(self.layoutWidget3)
        self.text_checkins.setObjectName(_fromUtf8("text_checkins"))
        self.gridLayout.addWidget(self.text_checkins, 3, 1, 1, 1)
        self.label_total_checkin = QtGui.QLabel(self.layoutWidget3)
        self.label_total_checkin.setObjectName(_fromUtf8("label_total_checkin"))
        self.gridLayout.addWidget(self.label_total_checkin, 3, 0, 1, 1)
        self.label_points = QtGui.QLabel(self.layoutWidget3)
        self.label_points.setObjectName(_fromUtf8("label_points"))
        self.gridLayout.addWidget(self.label_points, 2, 0, 1, 1)
        self.text_days = QtGui.QLabel(self.layoutWidget3)
        self.text_days.setObjectName(_fromUtf8("text_days"))
        self.gridLayout.addWidget(self.text_days, 1, 1, 1, 1)
        self.btn_open_home = QtGui.QLabel(self.layoutWidget3)
        self.btn_open_home.setOpenExternalLinks(False)
        self.btn_open_home.setObjectName(_fromUtf8("btn_open_home"))
        self.gridLayout.addWidget(self.btn_open_home, 3, 2, 1, 1)
        self.layoutWidget4 = QtGui.QWidget(self)
        self.layoutWidget4.setGeometry(QtCore.QRect(470, 440, 331, 131))
        self.layoutWidget4.setObjectName(_fromUtf8("layoutWidget4"))
        self.gridLayout_2 = QtGui.QGridLayout(self.layoutWidget4)
        self.gridLayout_2.setMargin(0)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.btn_send_msg = QtGui.QPushButton(self.layoutWidget4)
        self.btn_send_msg.setObjectName(_fromUtf8("btn_send_msg"))
        self.gridLayout_2.addWidget(self.btn_send_msg, 0, 0, 1, 1)
        self.chb_msg_group = QtGui.QCheckBox(self.layoutWidget4)
        self.chb_msg_group.setObjectName(_fromUtf8("chb_msg_group"))
        self.gridLayout_2.addWidget(self.chb_msg_group, 0, 2, 1, 1)
        self.textEdit_msg = QtGui.QPlainTextEdit(self.layoutWidget4)
        self.textEdit_msg.setObjectName(_fromUtf8("textEdit_msg"))
        self.gridLayout_2.addWidget(self.textEdit_msg, 1, 0, 1, 3)
        self.layoutWidget5 = QtGui.QWidget(self)
        self.layoutWidget5.setGeometry(QtCore.QRect(470, 590, 331, 34))
        self.layoutWidget5.setObjectName(_fromUtf8("layoutWidget5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.layoutWidget5)
        self.gridLayout_3.setMargin(0)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btn_kickout = QtGui.QPushButton(self.layoutWidget5)
        self.btn_kickout.setObjectName(_fromUtf8("btn_kickout"))
        self.gridLayout_3.addWidget(self.btn_kickout, 0, 0, 1, 1)
        self.chb_kickout_msg = QtGui.QCheckBox(self.layoutWidget5)
        self.chb_kickout_msg.setObjectName(_fromUtf8("chb_kickout_msg"))
        self.gridLayout_3.addWidget(self.chb_kickout_msg, 0, 3, 1, 1)
        self.chb_kickout_group = QtGui.QCheckBox(self.layoutWidget5)
        self.chb_kickout_group.setObjectName(_fromUtf8("chb_kickout_group"))
        self.gridLayout_3.addWidget(self.chb_kickout_group, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 1, 1, 1)

        self.set_ui_text()
        return None

    def set_ui_text(self):
        self.setWindowTitle("Shanbay Manage")
        self.btn_refresh.setText("刷新数据")
        self.label_refresh_time.setText("数据时间：00-00 12:12")
        self.label_recent_checkin.setText("最近七天打卡情况")
        self.btn_recent_checkin.setText("获取")
        self.chb_msg_group.setText("发送短信")
        self.btn_kickout.setText("踢出小组")
        self.text_points.setText("(N/A)")
        self.text_checkin.setText("(N/A)")
        self.text_nickname.setText("(N/A)")
        self.text_rank.setText("(N/A)")
        self.text_days.setText("(N/A)")
        self.text_rates.setText("(N/A)")
        self.label_days.setText("组龄：")
        self.label_nickname.setText("昵称：")
        self.label_checkin.setText("打卡：")
        self.label_points.setText("成长值：")
        self.label_rank.setText("排名：")
        self.label_rate.setText("打卡率：")
        self.label_recent_words.setText("最近七天背词情况")
        self.btn_recent_words.setText("获取")
        self.label_search.setText("搜索：")
        self.btn_group_add.setText(">>")
        self.btn_group_remove.setText("<<")
        self.btn_save_group.setText("保存列表")
        self.btn_open_home.setText("<a href=\"#open_home\" style=\" text-decoration: none;" +
                                   " color:#0000ff;\">打开空间</a>")
        self.text_checkins.setText("(N/A)")
        self.label_total_checkin.setText("总打卡：")
        self.label_total_checkin.setText("<a href=\"#total_checkin\" style=\" text-decoration: "
                                         "none; color:#000000;\">总打卡：</a>")
        self.btn_send_msg.setText("发站内信")
        self.chb_msg_group.setText("批量名单")
        self.btn_kickout.setText("踢出小组")
        self.chb_kickout_msg.setText("发站内信")
        self.chb_kickout_group.setText("批量名单")
        return None
    
    def tight_ui(self):
        self.setObjectName(_fromUtf8("UIMainWidget"))
        self.setWindowModality(QtCore.Qt.WindowModal)
        self.setEnabled(True)
        self.resize(885, 665)
        self.setMinimumSize(QtCore.QSize(814, 665))
        self.gridLayout_9 = QtGui.QGridLayout(self)
        self.gridLayout_9.setObjectName(_fromUtf8("gridLayout_9"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.gridLayout_5 = QtGui.QGridLayout()
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.cbb_team_condition = QtGui.QComboBox(self)
        self.cbb_team_condition.setObjectName(_fromUtf8("cbb_team_condition"))
        self.gridLayout_5.addWidget(self.cbb_team_condition, 2, 0, 1, 2)
        self.edit_search = QtGui.QLineEdit(self)
        self.edit_search.setObjectName(_fromUtf8("edit_search"))
        self.gridLayout_5.addWidget(self.edit_search, 0, 1, 1, 1)
        self.label_search = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Preferred, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_search.sizePolicy().hasHeightForWidth())
        self.label_search.setSizePolicy(sizePolicy)
        self.label_search.setObjectName(_fromUtf8("label_search"))
        self.gridLayout_5.addWidget(self.label_search, 0, 0, 1, 1)
        self.tb_members = QtGui.QTableWidget(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_members.sizePolicy().hasHeightForWidth())
        self.tb_members.setSizePolicy(sizePolicy)
        self.tb_members.setSizeIncrement(QtCore.QSize(0, 0))
        self.tb_members.setFrameShape(QtGui.QFrame.NoFrame)
        self.tb_members.setObjectName(_fromUtf8("tb_members"))
        self.tb_members.setColumnCount(0)
        self.tb_members.setRowCount(0)
        self.gridLayout_5.addWidget(self.tb_members, 1, 0, 1, 2)
        self.horizontalLayout.addLayout(self.gridLayout_5)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setSizeConstraint(QtGui.QLayout.SetFixedSize)
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        spacerItem = QtGui.QSpacerItem(20, 138, QtGui.QSizePolicy.Minimum,
                                       QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.btn_group_add = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_group_add.sizePolicy().hasHeightForWidth())
        self.btn_group_add.setSizePolicy(sizePolicy)
        self.btn_group_add.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_group_add.setObjectName(_fromUtf8("btn_group_add"))
        self.verticalLayout.addWidget(self.btn_group_add)
        spacerItem1 = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        self.verticalLayout.addItem(spacerItem1)
        self.btn_group_remove = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_group_remove.sizePolicy().hasHeightForWidth())
        self.btn_group_remove.setSizePolicy(sizePolicy)
        self.btn_group_remove.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_group_remove.setObjectName(_fromUtf8("btn_group_remove"))
        self.verticalLayout.addWidget(self.btn_group_remove)
        spacerItem2 = QtGui.QSpacerItem(20, 158, QtGui.QSizePolicy.Minimum,
                                        QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.gridLayout_4 = QtGui.QGridLayout()
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.cbb_group_list = QtGui.QComboBox(self)
        self.cbb_group_list.setObjectName(_fromUtf8("cbb_group_list"))
        self.gridLayout_4.addWidget(self.cbb_group_list, 0, 0, 1, 1)
        self.tb_group_selected = QtGui.QTableWidget(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tb_group_selected.sizePolicy().hasHeightForWidth())
        self.tb_group_selected.setSizePolicy(sizePolicy)
        self.tb_group_selected.setObjectName(_fromUtf8("tb_group_selected"))
        self.tb_group_selected.setColumnCount(0)
        self.tb_group_selected.setRowCount(0)
        self.gridLayout_4.addWidget(self.tb_group_selected, 1, 0, 1, 1)
        self.btn_save_group = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_save_group.sizePolicy().hasHeightForWidth())
        self.btn_save_group.setSizePolicy(sizePolicy)
        self.btn_save_group.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.btn_save_group.setFlat(False)
        self.btn_save_group.setObjectName(_fromUtf8("btn_save_group"))
        self.gridLayout_4.addWidget(self.btn_save_group, 2, 0, 1, 1)
        self.horizontalLayout.addLayout(self.gridLayout_4)
        self.verticalLayout_2 = QtGui.QVBoxLayout()
        self.verticalLayout_2.setObjectName(_fromUtf8("verticalLayout_2"))
        self.gridLayout = QtGui.QGridLayout()
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.text_checkin = QtGui.QLabel(self)
        self.text_checkin.setObjectName(_fromUtf8("text_checkin"))
        self.gridLayout.addWidget(self.text_checkin, 0, 3, 1, 1)
        self.text_points = QtGui.QLabel(self)
        self.text_points.setObjectName(_fromUtf8("text_points"))
        self.gridLayout.addWidget(self.text_points, 2, 1, 1, 1)
        self.label_nickname = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_nickname.sizePolicy().hasHeightForWidth())
        self.label_nickname.setSizePolicy(sizePolicy)
        self.label_nickname.setObjectName(_fromUtf8("label_nickname"))
        self.gridLayout.addWidget(self.label_nickname, 0, 0, 1, 1)
        self.text_rates = QtGui.QLabel(self)
        self.text_rates.setObjectName(_fromUtf8("text_rates"))
        self.gridLayout.addWidget(self.text_rates, 2, 3, 1, 1)
        self.text_rank = QtGui.QLabel(self)
        self.text_rank.setObjectName(_fromUtf8("text_rank"))
        self.gridLayout.addWidget(self.text_rank, 1, 3, 1, 1)
        self.label_rank = QtGui.QLabel(self)
        self.label_rank.setObjectName(_fromUtf8("label_rank"))
        self.gridLayout.addWidget(self.label_rank, 1, 2, 1, 1)
        self.label_checkin = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_checkin.sizePolicy().hasHeightForWidth())
        self.label_checkin.setSizePolicy(sizePolicy)
        self.label_checkin.setObjectName(_fromUtf8("label_checkin"))
        self.gridLayout.addWidget(self.label_checkin, 0, 2, 1, 1)
        self.label_days = QtGui.QLabel(self)
        self.label_days.setObjectName(_fromUtf8("label_days"))
        self.gridLayout.addWidget(self.label_days, 1, 0, 1, 1)
        self.text_nickname = QtGui.QLabel(self)
        self.text_nickname.setObjectName(_fromUtf8("text_nickname"))
        self.gridLayout.addWidget(self.text_nickname, 0, 1, 1, 1)
        self.label_rate = QtGui.QLabel(self)
        self.label_rate.setObjectName(_fromUtf8("label_rate"))
        self.gridLayout.addWidget(self.label_rate, 2, 2, 1, 1)
        self.text_checkins = QtGui.QLabel(self)
        self.text_checkins.setObjectName(_fromUtf8("text_checkins"))
        self.gridLayout.addWidget(self.text_checkins, 3, 1, 1, 1)
        self.label_total_checkin = QtGui.QLabel(self)
        self.label_total_checkin.setObjectName(_fromUtf8("label_total_checkin"))
        self.gridLayout.addWidget(self.label_total_checkin, 3, 0, 1, 1)
        self.label_points = QtGui.QLabel(self)
        self.label_points.setObjectName(_fromUtf8("label_points"))
        self.gridLayout.addWidget(self.label_points, 2, 0, 1, 1)
        self.text_days = QtGui.QLabel(self)
        self.text_days.setObjectName(_fromUtf8("text_days"))
        self.gridLayout.addWidget(self.text_days, 1, 1, 1, 1)
        self.btn_open_home = QtGui.QLabel(self)
        self.btn_open_home.setOpenExternalLinks(False)
        self.btn_open_home.setObjectName(_fromUtf8("btn_open_home"))
        self.gridLayout.addWidget(self.btn_open_home, 3, 2, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout)
        self.line = QtGui.QFrame(self)
        self.line.setFrameShape(QtGui.QFrame.HLine)
        self.line.setFrameShadow(QtGui.QFrame.Sunken)
        self.line.setObjectName(_fromUtf8("line"))
        self.verticalLayout_2.addWidget(self.line)
        self.gridLayout_recentWord = QtGui.QGridLayout()
        self.gridLayout_recentWord.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentWord.setObjectName(_fromUtf8("gridLayout_recentWord"))
        self.label_recent_words = QtGui.QLabel(self)
        self.label_recent_words.setObjectName(_fromUtf8("label_recent_words"))
        self.gridLayout_recentWord.addWidget(self.label_recent_words, 0, 0, 1, 1)
        self.btn_recent_words = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_words.sizePolicy().hasHeightForWidth())
        self.btn_recent_words.setSizePolicy(sizePolicy)
        self.btn_recent_words.setObjectName(_fromUtf8("btn_recent_words"))
        self.gridLayout_recentWord.addWidget(self.btn_recent_words, 0, 2, 1, 1)
        spacerItem3 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentWord.addItem(spacerItem3, 0, 1, 1, 1)
        self.tb_recent_words = QtGui.QTableWidget(self)
        self.tb_recent_words.setObjectName(_fromUtf8("tb_recent_words"))
        self.tb_recent_words.setColumnCount(0)
        self.tb_recent_words.setRowCount(0)
        self.gridLayout_recentWord.addWidget(self.tb_recent_words, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_recentWord)
        self.line_3 = QtGui.QFrame(self)
        self.line_3.setFrameShape(QtGui.QFrame.HLine)
        self.line_3.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_3.setObjectName(_fromUtf8("line_3"))
        self.verticalLayout_2.addWidget(self.line_3)
        self.gridLayout_recentCheckin = QtGui.QGridLayout()
        self.gridLayout_recentCheckin.setSizeConstraint(QtGui.QLayout.SetNoConstraint)
        self.gridLayout_recentCheckin.setObjectName(_fromUtf8("gridLayout_recentCheckin"))
        self.label_recent_checkin = QtGui.QLabel(self)
        self.label_recent_checkin.setObjectName(_fromUtf8("label_recent_checkin"))
        self.gridLayout_recentCheckin.addWidget(self.label_recent_checkin, 0, 0, 1, 1)
        self.btn_recent_checkin = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_recent_checkin.sizePolicy().hasHeightForWidth())
        self.btn_recent_checkin.setSizePolicy(sizePolicy)
        self.btn_recent_checkin.setObjectName(_fromUtf8("btn_recent_checkin"))
        self.gridLayout_recentCheckin.addWidget(self.btn_recent_checkin, 0, 2, 1, 1)
        spacerItem4 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_recentCheckin.addItem(spacerItem4, 0, 1, 1, 1)
        self.tb_recent_checkin = QtGui.QTableWidget(self)
        self.tb_recent_checkin.setObjectName(_fromUtf8("tb_recent_checkin"))
        self.tb_recent_checkin.setColumnCount(0)
        self.tb_recent_checkin.setRowCount(0)
        self.gridLayout_recentCheckin.addWidget(self.tb_recent_checkin, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_recentCheckin)
        self.line_4 = QtGui.QFrame(self)
        self.line_4.setFrameShape(QtGui.QFrame.HLine)
        self.line_4.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_4.setObjectName(_fromUtf8("line_4"))
        self.verticalLayout_2.addWidget(self.line_4)
        self.gridLayout_2 = QtGui.QGridLayout()
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        spacerItem5 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem5, 0, 1, 1, 1)
        self.btn_send_msg = QtGui.QPushButton(self)
        self.btn_send_msg.setObjectName(_fromUtf8("btn_send_msg"))
        self.gridLayout_2.addWidget(self.btn_send_msg, 0, 0, 1, 1)
        self.chb_msg_group = QtGui.QCheckBox(self)
        self.chb_msg_group.setObjectName(_fromUtf8("chb_msg_group"))
        self.gridLayout_2.addWidget(self.chb_msg_group, 0, 2, 1, 1)
        self.textEdit_msg = QtGui.QPlainTextEdit(self)
        self.textEdit_msg.setObjectName(_fromUtf8("textEdit_msg"))
        self.gridLayout_2.addWidget(self.textEdit_msg, 1, 0, 1, 3)
        self.verticalLayout_2.addLayout(self.gridLayout_2)
        self.line_5 = QtGui.QFrame(self)
        self.line_5.setFrameShape(QtGui.QFrame.HLine)
        self.line_5.setFrameShadow(QtGui.QFrame.Sunken)
        self.line_5.setObjectName(_fromUtf8("line_5"))
        self.verticalLayout_2.addWidget(self.line_5)
        self.gridLayout_3 = QtGui.QGridLayout()
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.btn_kickout = QtGui.QPushButton(self)
        self.btn_kickout.setObjectName(_fromUtf8("btn_kickout"))
        self.gridLayout_3.addWidget(self.btn_kickout, 0, 0, 1, 1)
        self.chb_kickout_msg = QtGui.QCheckBox(self)
        self.chb_kickout_msg.setObjectName(_fromUtf8("chb_kickout_msg"))
        self.gridLayout_3.addWidget(self.chb_kickout_msg, 0, 3, 1, 1)
        self.chb_kickout_group = QtGui.QCheckBox(self)
        self.chb_kickout_group.setObjectName(_fromUtf8("chb_kickout_group"))
        self.gridLayout_3.addWidget(self.chb_kickout_group, 0, 2, 1, 1)
        spacerItem6 = QtGui.QSpacerItem(40, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.gridLayout_3.addItem(spacerItem6, 0, 1, 1, 1)
        self.verticalLayout_2.addLayout(self.gridLayout_3)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.gridLayout_9.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.horizontalLayout_2 = QtGui.QHBoxLayout()
        self.horizontalLayout_2.setObjectName(_fromUtf8("horizontalLayout_2"))
        self.label_refresh_time = QtGui.QLabel(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_refresh_time.sizePolicy().hasHeightForWidth())
        self.label_refresh_time.setSizePolicy(sizePolicy)
        self.label_refresh_time.setMaximumSize(QtCore.QSize(300, 16777215))
        self.label_refresh_time.setObjectName(_fromUtf8("label_refresh_time"))
        self.horizontalLayout_2.addWidget(self.label_refresh_time)
        spacerItem7 = QtGui.QSpacerItem(488, 20, QtGui.QSizePolicy.Expanding,
                                        QtGui.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem7)
        self.btn_refresh = QtGui.QPushButton(self)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_refresh.sizePolicy().hasHeightForWidth())
        self.btn_refresh.setSizePolicy(sizePolicy)
        self.btn_refresh.setCheckable(False)
        self.btn_refresh.setObjectName(_fromUtf8("btn_refresh"))
        self.horizontalLayout_2.addWidget(self.btn_refresh)
        self.gridLayout_9.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)
        
        return
