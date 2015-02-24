#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import pyshanbay.page_parser as parser
import datetime


class Team:
    def __init__(self, shanbay):
        self.members_dict = {}
        self.shanbay = shanbay
        return

    def load(self):
        # get total page number of members
        self.members_dict.clear()
        main_page_members = self.shanbay.members_manage_page()
        total_page = parser.total_page_members(main_page_members)

        # get members info
        pages = []
        for page in range(1, int(total_page) + 1):
            page_html = self.shanbay.members_manage_page(page)
            pages.append(page_html)
        members_info = parser.parse_members_manage(pages)

        for member in members_info:
            self.members_dict[int(member['login_id'])] = member
        return None

    def get_page_count(self):
        self.members_dict.clear()
        main_page_members = self.shanbay.members_manage_page()
        total_page = parser.total_page_members(main_page_members)
        return int(total_page)

    def load_page(self, page_number):
        page_html = self.shanbay.members_manage_page(page_number)
        members_info = parser.parse_members_manage([page_html])
        for member in members_info:
            self.members_dict[int(member['login_id'])] = member
        return None

    def rank_points(self):
        members = list(self.members_dict.values())
        members = sorted(members, key=lambda x: int(x['points']), reverse=True)
        self.add_rank(members)
        return members

    def member(self, login_id):
        return self.members_dict[int(login_id)]

    def add_rank(self, ranked_members):
        for rank, member in enumerate(ranked_members):
            self.members_dict[int(member['login_id'])].update(
                {'rank': rank+1}
            )
        return None

    def add_total_checkins(self):
        for login_id, member in self.members_dict.items():
            page = self.shanbay.visit_member_home(login_id)
            checkins = parser.parse_total_checkin(page)
            member.update(
                {'checkins': checkins}
            )
        return None

    def member_home(self, login_id):
        return self.shanbay.get_member_home(login_id)

    def search(self, keyword):
        result = []
        for login_id, member in self.members_dict.items():
            if keyword in member['nickname']:
                result.append(member)
        result = sorted(result, key=lambda x: int(x['points']), reverse=True)
        return result

    def get_checkins(self, login_id):
        page = self.shanbay.visit_member_home(login_id)
        checkins = parser.parse_total_checkin(page)
        self.members_dict[int(login_id)].update(
            {'checkins': checkins}
        )
        return checkins

    def all_members(self):
        return list(self.members_dict.values())

    def kick_member(self, login_id_list):
        for login_id in login_id_list:
            self.members_dict.pop(int(login_id))
        return None

    def add_username(self, member):
        login_id = member['login_id']
        user_url = member['user_url']
        username = parser.parse_username(self.shanbay.visit_member_checkin(user_url))
        self.members_dict[int(login_id)].update(
            {'username': username}
        )
        return None

    def analyse_checkin_diary(self, member, max_absent_days):
        login_id = member['login_id']
        main_page = self.shanbay.visit_checkin_diary_main(login_id)
        username, total_checkin_days, diary_pages = \
            parser.parse_username_total_checkins_total_pages(main_page)
        self.members_dict[int(login_id)].update(
            {'checkins': total_checkin_days,
             'username': username}
        )

        # need to modify today
        date_end = datetime.date.today() + datetime.timedelta(days=-max_absent_days)
        checkin_dates = []

        stop = False
        for page_index in range(diary_pages):
            page_num = page_index + 1
            page = self.shanbay.visit_checkin_diary(login_id, page_num)
            dates_in_page = parser.parse_checkin_days(page)
            dates_in_page = sorted(dates_in_page, reverse=True)
            for checkin_date in dates_in_page:
                if checkin_date < date_end:
                    stop = True
                    break
                else:
                    checkin_dates.append(checkin_date)
            if stop is True:
                break

        self.members_dict[int(login_id)].update(
            {'checkin_dates': checkin_dates}
        )
        return

    def search_absent(self, absent_days):
        result = []
        date_end = datetime.date.today() + datetime.timedelta(days=-absent_days)
        for login_id, member in self.members_dict.items():
            try:
                checkin_days = member['checkin_dates']
            except KeyError:
                checkin_days = []
            checkin_days = sorted(checkin_days, reverse=True)
            if len(checkin_days) == 0:
                result.append(member)
            else:
                latest_checkin = checkin_days[0]
                if latest_checkin <= date_end:
                    result.append(member)
        return result




