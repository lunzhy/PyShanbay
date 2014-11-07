#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'


class Team:
    def __init__(self):
        self.members_dict = {}
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

        return