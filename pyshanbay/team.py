#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
import pyshanbay.page_parser as parser

class Team:
    def __init__(self, shanbay):
        self.members_dict = {}
        self.shanbay = shanbay
        return

    def load(self, members):
        self.members = members
        for member in self.members:
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