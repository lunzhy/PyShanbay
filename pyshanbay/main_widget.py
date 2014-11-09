#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from gui.ui_main import UIMainWidget
from pyshanbay.shanbay import VisitShanbay
from pyshanbay import page_parser as parser
from pyshanbay.team import Team
import datetime


class MainWidget(UIMainWidget):
    def __init__(self, config):
        super().__init__()
        self.config = config
        self.set_widget_property()
        # login shanbay
        self.shanbay = VisitShanbay(self.config.cfg_parser['Global']['username'],
                                    self.config.cfg_parser['Global']['password'])
        self.shanbay.login()
        self.team = Team(self.shanbay)

    @staticmethod
    def _change_date_style(origin_str):
        date = datetime.datetime.strptime(origin_str, '%Y-%m-%d')
        date_str = date.strftime('%m-%d')
        return date_str

    def set_widget_property(self):
        # set the tables
        self.tb_members.setColumnCount(5)  # login-id, rank, checked_today&yesterday, rate, nickname
        self.tb_members.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_members.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tb_members.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        # self.tb_members.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tb_members.verticalHeader().setVisible(False)
        self.tb_members.setColumnHidden(0, True)

        self.tb_members.setHorizontalHeaderLabels(['login id', '排名', '打卡', '打卡率', '昵称'])
        self.tb_members.setSortingEnabled(True)
        self.tb_members.setColumnWidth(1, 33)
        self.tb_members.setColumnWidth(2, 33)
        self.tb_members.setColumnWidth(3, 45)
        self.tb_members.horizontalHeader().setStretchLastSection(True)
        # self.tb_members.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.tb_recent_words.setRowCount(2)
        self.tb_recent_words.setColumnCount(7)
        self.tb_recent_words.setVerticalHeaderLabels(['已学', '要学'])
        self.tb_recent_words.setHorizontalHeaderLabels(['00-00'] * 7)
        self.tb_recent_words.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_recent_words.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        for i in range(7):
            self.tb_recent_words.setColumnWidth(i, 42)
        for i in range(2):
            self.tb_recent_words.setRowHeight(i, 27)
        self.tb_recent_words.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tb_recent_words.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)


        self.tb_recent_checkin.setRowCount(3)
        self.tb_recent_checkin.setColumnCount(7)
        self.tb_recent_checkin.setVerticalHeaderLabels(['单词', '文章', '句子'])
        self.tb_recent_checkin.setHorizontalHeaderLabels(['00-00'] * 7)
        self.tb_recent_checkin.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_recent_checkin.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        for i in range(7):
            self.tb_recent_checkin.setColumnWidth(i, 42)
        for i in range(3):
            self.tb_recent_checkin.setRowHeight(i, 28)
        self.tb_recent_checkin.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tb_recent_checkin.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.textEdit_msg.insertPlainText('The first line is the subject of the message.')

        # set the signals and slots
        self.tb_members.itemSelectionChanged.connect(self.selected_member)
        self.tb_members.itemClicked.connect(self.table_item_clicked)
        self.tb_members.itemSelectionChanged.connect(self.clear_table_recent)
        self.btn_refresh.clicked.connect(self.do_refresh_members)
        self.btn_recent_words.clicked.connect(self.do_set_recent_words)
        self.btn_recent_checkin.clicked.connect(self.do_set_recent_checkin)
        self.btn_kickout.clicked.connect(self.do_kickout_member)
        self.btn_send_msg.clicked.connect(self.do_send_message)
        self.btn_open_home.mousePressEvent = self.do_open_home
        self.label_total_checkin.mousePressEvent = self.do_click_checkins
        self.edit_search.textChanged.connect(self.do_search)
        return None

    def set_data_members(self, members_data):
        self.tb_members.setSortingEnabled(False)
        # sorting will conflict with the method of setting table item
        # self.tb_members.itemSelectionChanged.disconnect(self.selected_member)
        self.tb_members.setRowCount(len(members_data))
        for row_index, member in enumerate(members_data):
            new_item = QtGui.QTableWidgetItem(member['login_id'])
            self.tb_members.setItem(row_index, 0, new_item)

            new_item = QtGui.QTableWidgetItem()
            new_item.setData(QtCore.Qt.EditRole, int(member['rank']))
            self.tb_members.setItem(row_index, 1, new_item)

            today = 'O' if member['checkin_today'] is True else 'X'
            yesterday = 'O' if member['checkin_yesterday'] is True else 'X'
            check_text = '%s-%s' % (today, yesterday)
            new_item = QtGui.QTableWidgetItem(check_text)
            self.tb_members.setItem(row_index, 2, new_item)

            new_item = QtGui.QTableWidgetItem()
            rate = float(member['rate'].strip('%'))
            new_item.setData(QtCore.Qt.EditRole, rate)
            self.tb_members.setItem(row_index, 3, new_item)

            new_item = QtGui.QTableWidgetItem(str(member['nickname']))
            self.tb_members.setItem(row_index, 4, new_item)

        # bug: sorting the items will lead to blank rows
        self.tb_members.setSortingEnabled(True)
        return None

    def selected_member(self):
        ret = self._get_selected_loginid()
        if ret is False:
            self.clear_info_text()
        else:
            (login_id, row) = ret
            member = self.team.member(login_id)
            self.text_nickname.setText(member['nickname'])

            checkin = '%s | %s' % ('已打卡' if member['checkin_today'] else '未打卡',
                                   '已打卡' if member['checkin_yesterday'] else '未打卡')

            self.text_checkin.setText(checkin)
            self.text_days.setText(member['days'])
            self.text_rank.setText(str(member['rank']))
            self.text_points.setText(member['points'])
            self.text_rates.setText(member['rate'])
            try:
                self.text_checkins.setText(member['checkins'])
            except KeyError:
                self.text_checkins.setText('(N/A)')
                pass
        return None

    def do_refresh_members(self):
        self.tb_members.clearContents()
        self.edit_search.clear()
        datetime_str = self.shanbay.get_server_time().strftime('%Y-%m-%d %H:%M')
        text_time = '%s%s' % (self.label_refresh_time.text()[:5], datetime_str)
        self.label_refresh_time.setText(text_time)

        self.team.load()

        if self.config.cfg_parser['Data'].getboolean('total_checkin') is True:
            self.team.add_total_checkins()

        self.set_data_members(self.team.rank_points())
        self.tb_members.sortItems(1, QtCore.Qt.AscendingOrder)
        self.tb_members.clearSelection()
        self.tb_members.selectRow(0)
        return None

    def _get_selected_loginid(self):
        select = self.tb_members.selectionModel().selectedRows()
        try:
            row = select[0].row()
            login_id = self.tb_members.item(row, 0).text()
        except IndexError:
            return False
        return login_id, row

    def do_set_recent_words(self):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        page_progress = self.shanbay.get_progress(login_id)
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

    def do_set_recent_checkin(self):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        page_checkin = self.shanbay.get_checkin(login_id)
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

        words, reads, sents = [], [], []
        for index, day in enumerate(days_show):
            try:
                word = checkin_dict[day]['words']
                read = checkin_dict[day]['reads']
                sent = checkin_dict[day]['sents']
            except KeyError:
                word = 'N/A'
                read = 'N/A'
                sent = 'N/A'
            words.append(word)
            reads.append(read)
            sents.append(sent)

        self.tb_recent_checkin.setHorizontalHeaderLabels(days_show)

        for col_index, (word, read, sent) in enumerate(zip(words, reads, sents)):
            new_item = QtGui.QTableWidgetItem(str(word))
            self.tb_recent_checkin.setItem(0, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(read))
            self.tb_recent_checkin.setItem(1, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(sent))
            self.tb_recent_checkin.setItem(2, col_index, new_item)
        return None

    def clear_table_recent(self):
        self.tb_recent_checkin.clearContents()
        self.tb_recent_words.clearContents()
        return

    def do_kickout_member(self):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        member = self.team.member(login_id)

        if self.chb_kickout_msg.isChecked():
            msg = self.textEdit_msg.toPlainText()
            lines = msg.split('\n')
            try:
                subject = lines[0]
            except IndexError:
                subject = 'no subject'
            try:
                content = lines[1]
            except IndexError:
                content = 'no content'
            info = 'Are you sure to kick %s ?\n\n' \
                   'subject: %s\n' \
                   'content: %s' % (member['nickname'], subject, content)
        else:
            info = 'Are you sure to kick %s ?\n\n' \
                   'no message to send' % member['nickname']

        reply = QtGui.QMessageBox.question(self, 'Message', info,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            data_id = member['data_id']

            if self.chb_kickout_msg.isChecked():
                recipient = member['username']
                self.shanbay.send_message(recipient, subject, content)

            self.team.kick_member(login_id)
            self.tb_members.setRowHidden(row, True)
            self.shanbay.dismiss_member(data_id)
        return

    def do_send_message(self):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        member = self.team.member(login_id)

        msg = self.textEdit_msg.toPlainText()
        lines = msg.split('\n')
        try:
            subject = lines[0]
        except IndexError:
            subject = 'no subject'
        try:
            content = lines[1]
        except IndexError:
            content = 'no content'

        info = 'Are you sure to send message to %s ?\n\n' \
               'subject: %s\n' \
               'content: %s' % (member['nickname'], subject, content)

        reply = QtGui.QMessageBox.question(self, 'Message', info,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            recipient = member['username']
            self.shanbay.send_message(recipient, subject, content)
        return

    def do_open_home(self, ev):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        home = self.team.member_home(login_id)
        import webbrowser
        webbrowser.open(home)
        return None

    def do_search(self):
        text = self.edit_search.text().strip()
        if not len(text) is 0:
            search_result = self.team.search(str(text))

            self.tb_members.clearContents()
            self.set_data_members(search_result)
            self.clear_info_text()
            self.tb_members.clearSelection()
            self.tb_members.selectRow(0)
        else:
            self.tb_members.clearContents()
            self.set_data_members(self.team.all_members())
            self.tb_members.clearSelection()
            self.tb_members.selectRow(0)
        return None

    def clear_info_text(self):
        self.text_nickname.setText('N/A')
        self.text_checkin.setText('N/A')
        self.text_days.setText('N/A')
        self.text_rank.setText('N/A')
        self.text_points.setText('N/A')
        self.text_rates.setText('N/A')
        self.text_checkins.setText('N/A')
        pass

    def table_item_clicked(self, item):
        # TODO: item selection and clicking status requires improvement.
        row = item.row()
        self.tb_members.selectRow(-1)
        self.tb_members.selectRow(row)

    def do_click_checkins(self, ev):
        ret = self._get_selected_loginid()
        if ret is False:
            return None
        (login_id, row) = ret
        checkins = self.team.get_checkins(login_id)
        self.text_checkins.setText(str(checkins))
        return

if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MainWidget()
    main_form.show()
    app.exec_()