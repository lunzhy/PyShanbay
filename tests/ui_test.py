#! /usr/bin/env python3
# -*- coding: utf-8 -*- 
__author__ = 'Lunzhy'

import sys
from PyQt4.QtGui import *
from PyQt4.QtCore import *
from pyshanbay.shanbay import VisitShanbay
from pyshanbay import page_parser as parser
from gui.ui_main import UIMainWidget


class MainForm(QWidget):
    def __init__(self):
        super().__init__()
        self.table = QTableWidget()

        layout = QHBoxLayout()
        layout.addWidget(self.table)
        self.setLayout(layout)

        self.table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.table.verticalHeader().setResizeMode(QHeaderView.Fixed)
        self.table.itemClicked.connect(self.show_selected)

        return

    def set_data(self, members_data):
        self.table.setColumnCount(2)
        self.table.setRowCount(len(members_data))

        for row_index, member in enumerate(members_data):
            new_item = QTableWidgetItem(member['nickname'])
            self.table.setItem(row_index, 0, new_item)
            new_item = QTableWidgetItem(str(member['checked_today']))
            self.table.setItem(row_index, 1, new_item)
        return

    def show_selected(self):
        select = self.table.selectionModel().selectedRows()
        print(self.table.item(select[0].row(), 0).text())
        print(self.table.item(select[0].row(), 1).text())
        return


def get_data():
    shanbay = VisitShanbay()
    shanbay.login()

    page_members = shanbay.members()
    total_page = parser.total_page_members(page_members)

    pages = []

    for page in range(1, int(total_page) + 1):
        page_html = shanbay.members_page(page)
        pages.append(page_html)

    members_info = parser.parse_members_info(pages)
    return members_info


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_form = UIMainWidget()
    main_form.set_data_members(get_data())
    main_form.show()
    app.exec_()