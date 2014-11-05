#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from gui.ui_main import UIMainWidget
from pyshanbay.shanbay import VisitShanbay
from pyshanbay import page_parser as parser
import datetime


class MainWidget(UIMainWidget):
    def __init__(self):
        super().__init__()
        self.set_widget_property()
        self.members_data = []
        self.shanbay = VisitShanbay()
        return None


    @staticmethod
    def _change_date_style(origin_str):
        date = datetime.datetime.strptime(origin_str, '%Y-%m-%d')
        date_str = date.strftime('%m-%d')
        return date_str

    def set_widget_property(self):
        # set the tables
        self.tb_members.setColumnCount(2)
        self.tb_members.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_members.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tb_members.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        self.tb_members.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tb_members.setHorizontalHeaderLabels(['小组成员', '今日打卡'])

        self.tb_recent_words.setRowCount(2)
        self.tb_recent_words.setColumnCount(7)
        self.tb_recent_words.setVerticalHeaderLabels(['已学', '要学'])
        self.tb_recent_words.setHorizontalHeaderLabels(['00-00'] * 7)
        self.tb_recent_words.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_recent_words.setSelectionMode(QtGui.QAbstractItemView.NoSelection)

        self.tb_recent_checkin.setRowCount(2)
        self.tb_recent_checkin.setColumnCount(7)
        self.tb_recent_checkin.setVerticalHeaderLabels(['单词', '文章'])
        self.tb_recent_checkin.setHorizontalHeaderLabels(['00-00'] * 7)
        self.tb_recent_checkin.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_recent_checkin.setSelectionMode(QtGui.QAbstractItemView.NoSelection)

        # set the signals and slots
        self.tb_members.itemSelectionChanged.connect(self.selected_member)
        self.tb_members.itemSelectionChanged.connect(self.clear_table_data)
        self.btn_refresh.clicked.connect(self.set_data_members)
        self.btn_recent_words.clicked.connect(self.set_recent_words)
        self.btn_recent_checkin.clicked.connect(self.set_recent_checkin)
        return None

    def set_data_members(self):
        datetime_str = self.shanbay.get_server_time().strftime('%m-%d %H:%M')
        text_time = '%s%s' % (self.label_refresh_time.text()[:5], datetime_str)
        self.label_refresh_time.setText(text_time)

        self.refresh_members_data()
        self.tb_members.setRowCount(len(self.members_data))

        for row_index, member in enumerate(self.members_data):
            new_item = QtGui.QTableWidgetItem(member['nickname'])
            self.tb_members.setItem(row_index, 0, new_item)
            new_item = QtGui.QTableWidgetItem(str(member['checked_today']))
            self.tb_members.setItem(row_index, 1, new_item)
        self.tb_members.selectRow(0)
        return None

    def selected_member(self):
        select = self.tb_members.selectionModel().selectedRows()
        row = select[0].row()
        member = self.members_data[row]
        self.text_nickname.setText(member['nickname'])
        self.text_checkin.setText('已打卡' if member['checked_today'] else '未打卡')
        self.text_days.setText(member['days'])
        self.text_rank.setText(str(row + 1))
        self.text_points.setText(member['points'])
        self.text_rates.setText(member['rate'])
        return None

    def refresh_members_data(self):
        # log in shanbay.com
        self.shanbay.login()

        # get total page number of members
        main_page_members = self.shanbay.members()
        total_page = parser.total_page_members(main_page_members)

        # get members info
        pages = []
        for page in range(1, int(total_page) + 1):
            page_html = self.shanbay.members_page(page)
            pages.append(page_html)

        members_info = parser.parse_members_info(pages)
        self.members_data = members_info
        return None

    def _get_selected_userid(self):
        select = self.tb_members.selectionModel().selectedRows()
        row = select[0].row()
        member = self.members_data[row]
        userid = member['userid']
        return userid

    def set_recent_words(self):
        userid = self._get_selected_userid()
        page_progress = self.shanbay.get_progress(userid)
        nums_recent, revieweds_recent = parser.parse_recent_progress(page_progress)

        days = [recent[0] for recent in nums_recent]
        days = [self._change_date_style(day) for day in days]
        self.tb_recent_words.setHorizontalHeaderLabels(days)

        nums = [recent[1] for recent in nums_recent]
        rewieweds = [recent[1] for recent in revieweds_recent]

        for col_index, (day_num, day_reviewed) in enumerate(zip(nums, rewieweds)):
            new_item = QtGui.QTableWidgetItem(str(day_reviewed))
            self.tb_recent_words.setItem(0, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(day_num))
            self.tb_recent_words.setItem(1, col_index, new_item)
        return None

    def set_recent_checkin(self):
        page_checkin = self.shanbay.get_checkin(self._get_selected_userid())
        checkin_recent = parser.paser_checkin(page_checkin)

        checkin_dict = {}

        for checkin in checkin_recent:
            key = checkin[0].strftime('%m-%d')
            value = checkin[1]
            checkin_dict[key] = value

        today = self.shanbay.get_server_time()
        days_show = []
        for day_inc in range(7):
            day = today + datetime.timedelta(days=-day_inc)
            days_show.append(day.strftime('%m-%d'))


        words, reads = [], []
        for index, day in enumerate(days_show):
            try:
                word = checkin_dict[day]['words']
                read = checkin_dict[day]['reads']
            except KeyError:
                word = 'N/A'
                read = 'N/A'
            words.append(word)
            reads.append(read)

        self.tb_recent_checkin.setHorizontalHeaderLabels(days_show)

        for col_index, (word, read) in enumerate(zip(words, reads)):
            new_item = QtGui.QTableWidgetItem(str(word))
            self.tb_recent_checkin.setItem(0, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(read))
            self.tb_recent_checkin.setItem(1, col_index, new_item)
        return None

    def clear_table_data(self):
        self.tb_recent_checkin.clearContents()
        self.tb_recent_words.clearContents()
        return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MainWidget()
    main_form.show()
    app.exec_()