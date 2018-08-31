#! usr/bin /env python3
# -*- coding:utf-8 -*-
"""history entity"""

from conf import *


class History:

    def __init__(self, searched_pid, substituted_pid):
        # data format
        self.db_format = {
            "searched_pid": "searched_pid",
            "substituted_pid": "substituted_pid",
            "date": "CURRENT_TIMESTAMP"}
        # initiate data
        self.searched_pid = searched_pid
        self.substituted_pid = substituted_pid
        # initiate table
        self.table = HISTORY

    def create(self, entry):
        values = self.db_format
        values["searched_pid"] = self.searched_pid
        values["substituted_pid"] = self.substituted_pid
        table_name = self.table
        return values, table_name
