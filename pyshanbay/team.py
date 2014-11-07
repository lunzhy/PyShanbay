#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'


class Team:
    def __init__(self):
        self.members = []
        return

    def load(self, members):
        self.members = members
        return None

    def sort(self, keyword):
        # for keyword points currently
        members = sorted(self.members, key=lambda x: int(x['keyword']), reverse=True)
        self.members = members
        return self.members

    def rank_points(self):
        return

