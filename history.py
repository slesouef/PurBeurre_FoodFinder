#! usr/bin /env python3
# -*- coding:utf-8 -*-
"""history entity"""

from conf import *


class History:

    def __init__(self, pid=None, sub_pid=None):
        # data format
        self.db_format = {
            "pid": "pid",
            "sub_pid": "sub_pid",
            "date": "CURRENT_TIMESTAMP"}
        # initiate data
        self.pid = pid
        self.sub_pid = sub_pid
        # initiate table
        self.table = HISTORY

    def create(self):
        values = self.db_format
        values["pid"] = self.pid
        values["sub_pid"] = self.sub_pid
        table_name = self.table
        return values, table_name
