#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lunzhy'
import configparser
import datetime
import os


class ShanbayConfig:
    def __init__(self, filename='config.ini'):
        self.cfg_parser = configparser.ConfigParser()
        try:
            self.cfg_parser.read_file(open(filename))
        except FileNotFoundError:
            self.create_config(filename)
        return

    def create_config(self, filename):
        self.cfg_parser.add_section('Global')
        section = self.cfg_parser['Global']
        section['username'] = 'username'
        section['password'] = 'password'

        self.cfg_parser.add_section('Data')
        section = self.cfg_parser['Data']
        section['read_diary_days'] = '15'
        section['number_of_threads'] = '10'
        section['read_last_month'] = 'no'

        self.cfg_parser.add_section('Filter')
        section = self.cfg_parser['Filter']
        section['min_rate'] = '0.90'
        section['team_requirement'] = '21'

        with open(filename, 'w') as file:
            self.cfg_parser.write(file)
        return


class DismissLog:
    def __init__(self, min_rate, team_req, filename='group_list.log'):
        self.min_rate = min_rate
        self.team_req = team_req
        if os.path.exists('log') is not True:
            os.makedirs('log')
        self.log_file = os.path.join('log', filename)
        try:
            with open(self.log_file) as f:
                pass
        except FileNotFoundError:
            with open(self.log_file, 'w', encoding='utf8') as f:
                pass
        return

    def write_log(self, members, reason_index):
        with open(self.log_file, 'a', encoding='utf8') as f:
            now = datetime.datetime.now()
            f.write('[%s]\n' % now.strftime('%Y-%m-%d %H:%M:%S'))

            for member in members:
                nickname = member['nickname']
                rank = member['rank']
                rate = member['rate']
                days = member['days']
                line = '昵称：%s\t\t\t排名：%s\t\t组龄：%s\t\t打卡率：%s' % (nickname, rank, days, rate)
                if reason_index == 0:
                    reason = '未指定原因'
                elif reason_index == 1:
                    reason = '连续两天缺卡'
                elif reason_index == 2:
                    reason = '入组%s天未全部打卡' % self.team_req
                elif reason_index == 3:
                    reason = '打卡率低于%s%%' % str(self.min_rate)
                elif reason_index == 4:
                    reason = '上月全勤打卡'
                line = '%s\t\t原因：%s\n' % (line, reason)
                f.write(line)
            f.write('\n\n')
        return None


class DebugLog:
    def __init__(self, filename='debug.log'):
        self.log_file = filename
        with open(self.log_file, 'w+', encoding='utf8') as f:
            pass
        return

    def write_log(self, message):
        with open(self.log_file, 'a', encoding='utf8') as f:
            now = datetime.datetime.now()
            f.write('[%s]\n' % now.strftime('%Y-%m-%d %H:%M:%S'))
            f.write('%s\n' % message)
        return