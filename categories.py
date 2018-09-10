#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""categories entity"""

from conf import *


class Category:

    def __init__(self, name=None, cid=None):
        # data format
        self.db_format = {"name": "name", "cid": "cid"}
        # initialise data
        self.name = name
        self.cid = cid
        # initialise table
        self.table = CATEGORY

    def create(self):
        values = self.db_format
        values["name"] = self.name
        values["cid"] = self.cid
        table_name = self.table
        return values, table_name

    def update(self, entry, cid):
        data, table = entry
        data["cid"] = cid
        return entry
