#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'
from cx_Freeze import setup, Executable

includes = ["PyQt4"]
exe = Executable(
    script="main.py",
    targetName='ShanbayTeam.exe',
    base="Win32GUI",
    icon='icon.ico'
)

includefiles=['icon.ico', 'ask_for_leave.txt']
setup(
    name = "PyShanbay",
    options = {"build_exe": {"includes":includes, "include_files":includefiles}},
    executables = [exe]
)