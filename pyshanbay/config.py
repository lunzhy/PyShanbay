#! /usr/bin/env python3
# -*- coding: utf-8 -*-
__author__ = 'Lunzhy'
import configparser
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
        section['max_absent_days'] = '10'
        section['number_of_threads'] = '10'

        with open(filename, 'w') as file:
            self.cfg_parser.write(file)
        return