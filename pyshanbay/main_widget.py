#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import sys
from PyQt4 import QtGui
from PyQt4 import QtCore
from gui.ui_main import UIMainWidget
from pyshanbay.shanbay import VisitShanbay
from pyshanbay.config import DismissLog, DebugLog
from pyshanbay import page_parser as parser
from pyshanbay.team import Team
import datetime
import re
import time


class LoadTeamThread(QtCore.QThread):

    member_read = QtCore.pyqtSignal(str)
    member_read_finished = QtCore.pyqtSignal()

    def __init__(self, team):
        super(LoadTeamThread, self).__init__()
        self.team = team

    def run(self):
        pages_count = self.team.get_page_count()
        for index in range(pages_count):
            page_num = index + 1
            self.team.load_page(page_num)
            page_count_text = '%s/%s' % (page_num, pages_count)
            self.member_read.emit(page_count_text)
        self.member_read_finished.emit()


class UserDiaryThread(QtCore.QThread):

    diary_parsed = QtCore.pyqtSignal()

    def __init__(self, team, members, read_diary_days, debug_log):
        super(UserDiaryThread, self).__init__()
        self.team = team
        self.read_diary_days = read_diary_days
        self.members = members
        self.debug_log = debug_log
        self.failed_members = []  # the members that current thread fails to read

    def run(self):
        parse_members = self.members
        self.read(parse_members)

    def read(self, members_to_parse):
        self.failed_members = []
        for index, member in enumerate(members_to_parse):
            try:
                self.team.analyse_checkin_diary(member, self.read_diary_days)
                self.diary_parsed.emit()
            except:
                self.debug_log.write_log('exception in parsing %s' % member['nickname'])
                self.failed_members.append(member)

        if len(self.failed_members) == 0:
            return None
        reload_nicknames = ','.join([member['nickname'] for member in self.failed_members])
        self.debug_log.write_log('reload: %s' % reload_nicknames)
        time.sleep(10)
        self.read(self.failed_members)
        return None


class MainWidget(UIMainWidget):
    def __init__(self, config, debug_log):
        super().__init__()
        self.refresh_time = ''
        self.config = config
        self.set_widget_property()

        # login shanbay
        self.shanbay = VisitShanbay(self.config.cfg_parser['Global']['username'],
                                    self.config.cfg_parser['Global']['password'])
        self.shanbay.login()
        self.team = Team(self.shanbay)
        self.group_list = []
        self.diary_all_loaded = False

        self.full_last_month = self.config.cfg_parser['Data'].getboolean('read_last_month')
        self.read_diary_days = self.team.get_read_diary_day(self.config)

        self.team_req = self.config.cfg_parser['Filter'].getint('team_requirement')
        self.min_rate = self.config.cfg_parser['Filter'].getfloat('min_rate') * 100

        date_str = datetime.date.today().strftime('%Y-%m-%d.txt')
        self.dismiss_log = DismissLog(self.min_rate, self.team_req, filename=date_str)

        # manipulate the threads
        self.load_team_thread = LoadTeamThread(self.team)
        self.load_team_thread.member_read.connect(self.refresh_read_member)
        self.load_team_thread.member_read_finished.connect(self.do_refresh_table_members)

        self.diary_threads = []
        self.diary_parsed_count = 0

        self.debug_log = debug_log

        self.update_ui()

    def update_ui(self):
        txt_absent_days = "%s%s" % (self.read_diary_days, self.label_absent_days.text()[2:])
        self.label_absent_days.setText(txt_absent_days)
        txt_absent_days = "%s%s" % (self.read_diary_days, self.label_search_absent.text()[2:])
        self.label_search_absent.setText(txt_absent_days)

        self.cbb_group_list.addItem('--请选择筛选条件--')
        self.cbb_group_list.addItem('连续两天缺卡')
        self.cbb_group_list.addItem('组龄小于%s天查卡日缺卡' % self.team_req)
        self.cbb_group_list.addItem('打卡率低于%s%%' % str(self.min_rate))
        if self.full_last_month is True:
            self.cbb_group_list.addItem('上月全勤打卡')
        return None

    @staticmethod
    def _change_date_style(origin_str):
        date = datetime.datetime.strptime(origin_str, '%Y-%m-%d')
        date_str = date.strftime('%m-%d')
        return date_str

    def assemble_message(self, msg_text, member):
        patt = re.compile(r'(?<=\[).*?(?=\])')
        keys = patt.findall(msg_text)
        if len(keys) == 0:
            return msg_text
        else:
            new_text = msg_text
            for key in keys:
                patt = re.compile(r'\[%s\]' % key)
                try:
                    new_text = re.sub(patt, str(member[key]), new_text)
                except KeyError:
                    self.team.analyse_checkin_diary(member, self.read_diary_days)
                    try:
                        new_text = re.sub(patt, str(member[key]), new_text)
                    except KeyError:
                        pass

        return new_text

    def set_widget_property(self):
        # set the members tables
        self.tb_members.setColumnCount(6)
        # login-id, rank, checked_today&yesterday, rate, days,nickname
        self.tb_members.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_members.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tb_members.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        # self.tb_members.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tb_members.verticalHeader().setVisible(False)

        headers = ['login id', '排名', '打卡', '打卡率', '组龄', '昵称']
        self.tb_members.setHorizontalHeaderLabels(headers)
        self.tb_members.setSortingEnabled(True)
        self.tb_members.setColumnHidden(0, True)
        self.tb_members.setColumnWidth(1, 33)
        self.tb_members.setColumnWidth(2, 33)
        self.tb_members.setColumnWidth(3, 45)
        self.tb_members.setColumnWidth(4, 33)
        self.tb_members.horizontalHeader().setStretchLastSection(True)
        # self.tb_members.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        # set group table
        self.tb_group.setColumnCount(7)  # login-id, rank, checked_today&yesterday,
        # rate, nickname
        self.tb_group.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_group.setSelectionBehavior(QtGui.QAbstractItemView.SelectRows)
        self.tb_group.setSelectionMode(QtGui.QAbstractItemView.SingleSelection)
        # self.tb_members.verticalHeader().setResizeMode(QtGui.QHeaderView.Fixed)
        self.tb_group.verticalHeader().setVisible(False)

        headers = ['login id', '排名', '打卡', '打卡率', '组龄', '缺卡', '昵称']
        self.tb_group.setHorizontalHeaderLabels(headers)
        self.tb_group.setSortingEnabled(True)
        self.tb_group.setColumnHidden(0, True)
        self.tb_group.setColumnWidth(1, 33)
        self.tb_group.setColumnWidth(2, 33)
        self.tb_group.setColumnWidth(3, 45)
        self.tb_group.setColumnWidth(4, 33)
        self.tb_group.setColumnWidth(5, 33)
        self.tb_group.horizontalHeader().setStretchLastSection(True)

        # set other tables
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

        self.tb_recent_checkin.setRowCount(4)
        self.tb_recent_checkin.setColumnCount(7)
        self.tb_recent_checkin.setVerticalHeaderLabels(['单词', '文章', '句子', '听力'])
        self.tb_recent_checkin.setHorizontalHeaderLabels(['00-00'] * 7)
        self.tb_recent_checkin.setEditTriggers(QtGui.QAbstractItemView.NoEditTriggers)
        self.tb_recent_checkin.setSelectionMode(QtGui.QAbstractItemView.NoSelection)
        for i in range(7):
            self.tb_recent_checkin.setColumnWidth(i, 42)
        for i in range(3):
            self.tb_recent_checkin.setRowHeight(i, 29)
        self.tb_recent_checkin.horizontalHeader().setResizeMode(QtGui.QHeaderView.Stretch)
        self.tb_recent_checkin.verticalHeader().setResizeMode(QtGui.QHeaderView.Stretch)

        self.textEdit_msg.insertPlainText('The first line is the subject of the message.')

        # set the signals and slots
        self.tb_members.itemSelectionChanged.connect(self.selected_member)
        # self.tb_members.itemClicked.connect(self.table_item_clicked)
        self.tb_members.itemSelectionChanged.connect(self.clear_table_recent)
        self.btn_refresh.clicked.connect(self.load_team)
        self.btn_recent_words.clicked.connect(self.do_set_recent_words)
        self.btn_recent_checkin.clicked.connect(self.do_set_recent_checkin)
        self.btn_kickout.clicked.connect(self.do_kickout_member)
        self.btn_send_msg.clicked.connect(self.do_send_message)
        self.btn_open_home.mousePressEvent = self.do_open_home
        self.label_total_checkin.mousePressEvent = self.do_click_checkins
        self.edit_search.textChanged.connect(self.do_search)
        self.btn_group_add.clicked.connect(self.do_add_group)
        self.btn_group_remove.clicked.connect(self.do_remove_group)
        self.btn_absent_days.clicked.connect(self.do_search_absent)
        self.btn_clear_group.clicked.connect(self.do_clear_group)

        self.tb_group.itemSelectionChanged.connect(self.selected_member)
        self.tb_group.itemSelectionChanged.connect(self.clear_table_recent)
        # it is sufficient to only connect one radio button
        self.rbtn_group.toggled.connect(self.selected_member)
        self.rbtn_group.toggled.connect(self.clear_table_recent)

        self.tb_members.mouseDoubleClickEvent = self.do_double_click_member_table
        self.tb_group.mouseDoubleClickEvent = self.do_double_click_group_table

        self.btn_group_filter.clicked.connect(self.do_filter)
        self.btn_show_leave.toggled.connect(self.do_show_leave)
        self.btn_save_group.clicked.connect(self.do_save_group)
        return None

    def set_table_data(self, table_to_set, members_data):
        table_to_set.setSortingEnabled(False)

        # sorting will conflict with the method of setting table item
        # self.tb_members.itemSelectionChanged.disconnect(self.selected_member)

        table_to_set.setRowCount(len(members_data))
        for row_index, member in enumerate(members_data):
            new_item = QtGui.QTableWidgetItem(member['login_id'])
            table_to_set.setItem(row_index, 0, new_item)

            new_item = QtGui.QTableWidgetItem()
            new_item.setData(QtCore.Qt.EditRole, int(member['rank']))
            table_to_set.setItem(row_index, 1, new_item)

            today = 'O' if member['checkin_today'] is True else 'X'
            yesterday = 'O' if member['checkin_yesterday'] is True else 'X'
            check_text = '%s-%s' % (today, yesterday)
            new_item = QtGui.QTableWidgetItem(check_text)
            table_to_set.setItem(row_index, 2, new_item)

            new_item = QtGui.QTableWidgetItem()
            rate = float(member['rate'].strip('%'))
            new_item.setData(QtCore.Qt.EditRole, rate)
            table_to_set.setItem(row_index, 3, new_item)

            new_item = QtGui.QTableWidgetItem()
            new_item.setData(QtCore.Qt.EditRole, int(member['days']))
            table_to_set.setItem(row_index, 4, new_item)

            if table_to_set == self.tb_group:
                try:
                    absent_days = member['absent']
                except KeyError:
                    # read_diary_days = self.read_diary_days
                    # self.team.get_absent_days(member, read_diary_days)
                    absent_days = 'N/A'

                new_item = QtGui.QTableWidgetItem(str(absent_days))
                table_to_set.setItem(row_index, 5, new_item)

                new_item = QtGui.QTableWidgetItem()
                new_item.setData(QtCore.Qt.EditRole, str(member['nickname']))
                table_to_set.setItem(row_index, 6, new_item)

            elif table_to_set == self.tb_members:
                new_item = QtGui.QTableWidgetItem(str(member['nickname']))
                table_to_set.setItem(row_index, 5, new_item)

        # bug: sorting the items will lead to blank rows
        table_to_set.setSortingEnabled(True)
        return None

    def selected_member(self):
        ret = self._get_selected_loginid()
        if ret is False:
            self.clear_info_text()
        else:
            (login_id, row) = ret
            member = self.team.member(login_id)
            self.text_nickname.setText(str(member['nickname']))

            checkin = '%s | %s' % ('已打卡' if member['checkin_today'] else '未打卡',
                                   '已打卡' if member['checkin_yesterday'] else '未打卡')

            self.text_checkin.setText(checkin)
            self.text_days.setText(str(member['days']))
            self.text_rank.setText(str(member['rank']))
            self.text_points.setText(str(member['points']))
            self.text_rates.setText(str(member['rate']))
            try:
                self.text_checkins.setText(str(member['checkins']))
            except KeyError:
                self.text_checkins.setText('(N/A)')
                pass

            try:
                self.text_absent_days.setText(str(member['absent']))
            except KeyError:
                self.text_absent_days.setText('(N/A)')
                pass
        return None

    def do_refresh_table_members(self):
        datetime_str = self.shanbay.get_server_time().strftime('%Y-%m-%d %H:%M')
        text_time = '%s%s' % (self.label_refresh_time.text()[:5], datetime_str)
        self.refresh_time = text_time

        self.set_table_data(self.tb_members, self.team.rank_points())
        self.tb_members.sortItems(1, QtCore.Qt.AscendingOrder)
        self.tb_members.clearSelection()
        self.tb_members.selectRow(0)

        self.label_refresh_time.setText(self.refresh_time)

        self.btn_refresh.setEnabled(True)
        self.edit_search.setEnabled(True)

        self.load_user_diary()
        return None

    def _get_selected_loginid(self, table_to_select=None):
        if table_to_select is None:
            if self.rbtn_member.isChecked():
                table_to_select = self.tb_members
            elif self.rbtn_group.isChecked():
                table_to_select = self.tb_group

        if table_to_select is None:
            table_to_select = self.tb_members

        select = table_to_select.selectionModel().selectedRows()
        try:
            row = select[0].row()
            login_id = table_to_select.item(row, 0).text()
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
        checkin_recent = parser.parse_checkin(page_checkin)

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

        words, reads, sents, lstns = [], [], [], []
        for index, day in enumerate(days_show):
            try:
                word = checkin_dict[day]['words']
            except KeyError:
                word = 'N/A'

            try:
                read = checkin_dict[day]['reads']
            except KeyError:
                read = 'N/A'

            try:
                sent = checkin_dict[day]['sents']
            except KeyError:
                sent = 'N/A'

            try:
                lstn = checkin_dict[day]['lstns']
            except KeyError:
                lstn = 'N/A'

            words.append(word)
            reads.append(read)
            sents.append(sent)
            lstns.append(lstn)

        self.tb_recent_checkin.setHorizontalHeaderLabels(days_show)

        for col_index, (word, read, sent, lstn) in enumerate(zip(words, reads, sents, lstns)):
            new_item = QtGui.QTableWidgetItem(str(word))
            self.tb_recent_checkin.setItem(0, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(read))
            self.tb_recent_checkin.setItem(1, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(sent))
            self.tb_recent_checkin.setItem(2, col_index, new_item)
            new_item = QtGui.QTableWidgetItem(str(lstn))
            self.tb_recent_checkin.setItem(3, col_index, new_item)
        return None

    def clear_table_recent(self):
        self.tb_recent_checkin.clearContents()
        self.tb_recent_words.clearContents()
        return

    def do_kickout_member(self):
        members_to_kick = ()
        if self.chb_kickout_group.isChecked():
            row_count = self.tb_group.rowCount()
            # print('group', self.tb_group.rowCount())
            if row_count == 0:
                return None
            for row in range(row_count):
                login_id = self.tb_group.item(row, 0).text()
                member = self.team.member(login_id)
                members_to_kick += (member,)

        else:
            # print('single')
            ret = self._get_selected_loginid()
            if ret is False:
                return None
            (login_id, row) = ret
            member = self.team.member(login_id)
            members_to_kick += (member,)

        for member in members_to_kick:
            if len(member['username']) == 0:
                # info = 'Username for %s has not been obtained.\n' \
                # 'Please wait for a moment.' % member['nickname']
                # QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
                # return
                self.team.add_username(member)

        kickouts = [member['username'] for member in members_to_kick]

        if len(members_to_kick) > 20:
            nicknames = ', '.join([member['nickname'] for member in members_to_kick[:20]])
            nicknames += ', ... ... (totally %s members)' % len(members_to_kick)
        else:
            nicknames = ', '.join([member['nickname'] for member in members_to_kick])

        kick_ids = [member['data_id'] for member in members_to_kick]
        login_ids = [member['login_id'] for member in members_to_kick]

        # print(kickouts, nicknames)

        if self.chb_kickout_msg.isChecked():
            msg = self.textEdit_msg.toPlainText()
            lines = msg.split('\n')
            try:
                subject = lines[0]
            except IndexError:
                subject = 'no subject'
            try:
                content = '\n'.join(lines[1:])
            except IndexError:
                content = 'no content'
            info = 'Are you sure to kick\n' \
                   '%s ?\n\n' \
                   'subject: %s\n' \
                   'content: %s' % (nicknames, subject, content)
        else:
            info = 'Are you sure to kick\n' \
                   '%s ?\n\n' \
                   'no message to send' % nicknames
        reply = QtGui.QMessageBox.question(self, 'Message', info,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.No:
            return None
        info = 'Are you sure to kick\n%s ?\n\n' % nicknames

        double_check_reply = QtGui.QMessageBox.question(self, 'Double Check', info,
                                    QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                    QtGui.QMessageBox.No)
        if double_check_reply == QtGui.QMessageBox.No:
            return None

        if self.chb_kickout_msg.isChecked():
            for member, kickout in zip(members_to_kick, kickouts):
                user_content = self.assemble_message(content, member)
                self.shanbay.send_message(kickout, subject, user_content)

        # remove the rows in the tables, remove the row in group list first
        for kick_id in login_ids:
            # remove the row in group table
            row_to_kick = None
            for row_index in range(self.tb_group.rowCount()):
                login_id = self.tb_group.item(row_index, 0).text()
                if login_id == kick_id:
                    row_to_kick = row_index
                    break
            if row_to_kick is not None:
                self.tb_group.removeRow(row_to_kick)
                member = self.team.member(kick_id)
                self.group_list.remove(member)

            # remove the row in member table
            row_to_kick = None
            for row_index in range(self.tb_members.rowCount()):
                login_id = self.tb_members.item(row_index, 0).text()
                if login_id == kick_id:
                    row_to_kick = row_index
                    break
            if row_to_kick is not None:
                self.tb_members.removeRow(row_to_kick)

        self.team.kick_member(login_ids)
        self.diary_parsed_count -= len(login_ids)

        self.shanbay.dispel_member(kick_ids)
        return

    def do_send_message(self):
        members_to_send = ()
        if self.chb_msg_group.isChecked():
            row_count = self.tb_group.rowCount()
            if row_count == 0:
                return None
            for row in range(row_count):
                login_id = self.tb_group.item(row, 0).text()
                member = self.team.member(login_id)
                members_to_send += (member,)
        else:
            ret = self._get_selected_loginid()
            if ret is False:
                return None
            (login_id, row) = ret
            member = self.team.member(login_id)
            members_to_send += (member,)

        for member in members_to_send:
            if len(member['username']) == 0:
                # info = 'Username for %s has not been obtained.\n' \
                #       'Please wait for a moment.' % member['nickname']
                # QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
                # return
                self.team.add_username(member)

        recipients = [member['username'] for member in members_to_send]

        if len(members_to_send) > 20:
            nicknames = ', '.join([member['nickname'] for member in members_to_send[:20]])
            nicknames += ', ... ... (totally %s members)' % len(members_to_send)
        else:
            nicknames = [member['nickname'] for member in members_to_send]
            nicknames = ', '.join(nicknames)

        msg = self.textEdit_msg.toPlainText()
        lines = msg.split('\n')
        try:
            subject = lines[0]
        except IndexError:
            subject = 'no subject'
        try:
            content = '\n'.join(lines[1:])
        except IndexError:
            content = 'no content'

        info = 'Are you sure to send message to\n' \
               '%s ?\n\n' \
               'subject: %s\n' \
               'content: %s' % (nicknames, subject, content)

        reply = QtGui.QMessageBox.question(self, 'Message', info,
                                           QtGui.QMessageBox.Yes | QtGui.QMessageBox.No,
                                           QtGui.QMessageBox.No)
        if reply == QtGui.QMessageBox.Yes:
            for member, recipient in zip(members_to_send, recipients):
                user_content = self.assemble_message(content, member)
                self.shanbay.send_message(recipient, subject, user_content)
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
        if not len(text) == 0:
            search_result = self.team.search(str(text))

            self.tb_members.clearContents()
            self.set_table_data(self.tb_members, search_result)
            self.clear_info_text()
            self.tb_members.clearSelection()
            self.tb_members.selectRow(0)
        else:
            self.tb_members.clearContents()
            self.set_table_data(self.tb_members, self.team.all_members())
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
        self.text_absent_days.setText('N/A')
        return None

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
        return None

    def load_team(self):
        self.team.clear()
        self.set_table_data(self.tb_members, [])
        self.set_table_data(self.tb_group, [])
        self.diary_all_loaded = False
        self.diary_parsed_count = 0
        self.group_list.clear()
        self.clear_info_text()
        self.clear_table_recent()
        self.edit_search.clear()
        self.btn_refresh.setEnabled(False)
        self.edit_search.setEnabled(False)
        self.load_team_thread.start()
        return None

    def refresh_diary_count(self, text):
        new_text = r'%s%s' % (self.label_get_diary.text()[:5], text)
        self.label_get_diary.setText(new_text)
        return None

    def refresh_read_member(self, text):
        new_text = r'%s%s' % (self.label_read_member.text()[:5], text)
        self.label_read_member.setText(new_text)
        return None

    def do_add_group(self):
        ret = self._get_selected_loginid(self.tb_members)
        if ret is False:
            return None
        (login_id, row) = ret
        member = self.team.member(login_id)

        group_loginid = [mem['login_id'] for mem in self.group_list]
        if member['login_id'] in group_loginid:
            return None

        self.group_list += [member]
        self.set_table_data(self.tb_group, self.group_list)
        return None

    def do_remove_group(self):
        ret = self._get_selected_loginid(self.tb_group)
        if ret is False:
            return None
        (login_id, row) = ret
        member = self.team.member(login_id)

        self.group_list.remove(member)
        self.tb_group.removeRow(row)
        return None

    def do_search_absent(self):
        diary_loaded = True if self.diary_parsed_count == len(self.team.all_members()) else False

        if diary_loaded is not True:
            info = 'Please wait until all the checkin diaries are parsed.'
            QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
            return None

        read_diary_days = self.read_diary_days
        try:
            absent_days = int(self.edit_absent_days.text())
            if (0 <= absent_days <= read_diary_days) is not True:
                raise ValueError
        except ValueError:
            info = 'Please input a number between 0 and %s .' % read_diary_days
            QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
            return None

        self.do_clear_group()
        search_results = self.team.search_absent(absent_days)
        self.group_list = search_results
        self.set_table_data(self.tb_group, search_results)
        return None

    def do_clear_group(self):
        self.group_list.clear()
        self.tb_group.clearContents()
        self.set_table_data(self.tb_group, [])
        return None

    def load_user_diary(self):
        self.diary_parsed_count = 0
        [thread.quit() for thread in self.diary_threads]
        self.diary_threads = []

        read_diary_days = self.read_diary_days
        number_of_threads = self.config.cfg_parser['Data'].getint('number_of_threads')

        all_members = self.team.all_members()
        total_members_count = len(all_members)

        if total_members_count % number_of_threads == 0:
            threads_capacity = int(total_members_count / number_of_threads)
        else:
            threads_capacity = total_members_count // number_of_threads

        full = total_members_count // threads_capacity

        for index in range(full):
            members = all_members[index*threads_capacity: (index+1)*threads_capacity]
            self.diary_threads.append(
                UserDiaryThread(self.team, members, read_diary_days, self.debug_log)
            )
        members = all_members[threads_capacity*full:]
        self.diary_threads.append(
            UserDiaryThread(self.team, members, read_diary_days, self.debug_log))

        for thread in self.diary_threads:
            thread.diary_parsed.connect(self._user_diary_parsed)

        for thread in self.diary_threads:
            thread.start()
        return None

    def _user_diary_parsed(self):
        total_count = len(self.team.all_members())
        title_text = self.label_get_diary.text()[:5]
        self.diary_parsed_count += 1
        finished = '%s%s/%s' % (title_text, self.diary_parsed_count, total_count)
        self.label_get_diary.setText(finished)

        diary_loaded = True if self.diary_parsed_count == len(self.team.all_members()) else False
        if diary_loaded is True:
            self.diary_all_loaded = True
            self.find_early_checkin_member()
        return None

    def do_double_click_member_table(self, event):
        if self.rbtn_member.isChecked() is not True:
            self.rbtn_member.click()
        if event.button() == QtCore.Qt.LeftButton:
            self.do_set_recent_words()
        elif event.button() == QtCore.Qt.RightButton:
            self.do_set_recent_checkin()
        return None

    def do_double_click_group_table(self, event):
        if self.rbtn_group.isChecked() is not True:
            self.rbtn_group.click()
        if event.button() == QtCore.Qt.LeftButton:
            self.do_set_recent_words()
        elif event.button() == QtCore.Qt.RightButton:
            self.do_set_recent_checkin()
        return None

    def find_early_checkin_member(self):
        for row_index in range(self.tb_group.rowCount()):
            login_id = self.tb_group.item(row_index, 0).text()
            early = self.team.member(login_id)['early_checkin']
            if early is True:
                for col in range(self.tb_members.columnCount()):
                    self.tb_members.item(row_index, col).setBackground(
                        QtGui.QColor(255, 0, 0))
        return None

    def do_filter(self):
        if self.diary_all_loaded is False:
            info = 'Please wait until all the checkin diaries are parsed.'
            QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
            return None

        current_index = self.cbb_group_list.currentIndex()
        count_today = 0 if self.chb_manage_day.isChecked() is True else 1

        if current_index == 0:
            return None

        filter_results = []
        self.do_clear_group()

        if current_index == 1:  # absent for two days
            filter_results = self.team.filter_absent_two_days(count_today)
        elif current_index == 2:  # new member
            filter_results = self.team.filter_new_member(self.team_req, count_today)
        elif current_index == 3:  # rate
            filter_results = self.team.filter_rate(self.min_rate)
        elif current_index == 4:  # full last month
            filter_results = self.team.filter_full_last_month()

        self.group_list = filter_results
        self.set_table_data(self.tb_group, filter_results)
        return None

    def do_show_leave(self):
        try:
            leave_nicknames = self.team.load_leave_list()
        except FileNotFoundError:
            info = 'The file for member asking for leave [ask_for_leave.txt] does not exist.'
            QtGui.QMessageBox.warning(self, 'Warning', info, QtGui.QMessageBox.Yes)
            return None

        if self.tb_group.rowCount() == 0:
            self.btn_show_leave.setChecked(False)
            return None

        if self.btn_show_leave.isChecked():
            color = QtGui.QColor(255, 255, 0)
        else:  # not checked
            color = QtGui.QColor(255, 255, 255)

        row_count = self.tb_group.rowCount()
        for row_index in range(row_count):
            nickname = self.tb_group.item(row_index, 6).text()  # column 6 for nickname
            if nickname in leave_nicknames:
                col_count = self.tb_group.columnCount()
                for col_index in range(col_count):
                    self.tb_group.item(row_index, col_index).setBackground(color)
        return None

    def do_save_group(self):
        if len(self.group_list) == 0:
            return None
        filter_index = self.cbb_group_list.currentIndex()
        self.dismiss_log.write_log(self.group_list, filter_index)
        info = 'Write the group list to log file.'
        QtGui.QMessageBox.warning(self, 'Done', info, QtGui.QMessageBox.Yes)
        return None


if __name__ == '__main__':
    app = QtGui.QApplication(sys.argv)
    main_form = MainWidget()
    main_form.show()
    app.exec_()