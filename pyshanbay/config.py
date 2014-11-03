#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lunzhy'
import configparser
import os


class ShanbayConfig:
    def __init__(self, filename='config.ini'):
        self.config = configparser.ConfigParser()
        try:
            self.config.read_file(open(filename))
        except FileNotFoundError:
            self.create_config(filename)
        return

    def create_config(self, filename):
        self.config.add_section('Global')
        section = self.config['Global']
        section['username'] = 'ibluecoffee'
        section['password'] = '870625@shanbay'
        with open(filename, 'w') as file:
            self.config.write(file)
        return