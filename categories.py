#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""categories entity"""

from conf import *


class Category:

    def __init__(self, name=None, id=None):
        # data format
        self.db_format = {"name": "name", "id": "id"}
        # initialise data
        self.name = name
        self.id = id
        # initialise table
        self.table = CATEGORY

    def create(self):
        values = self.db_format
        values["name"] = self.name
        values["id"] = self.id
        table_name = self.table
        return values, table_name

    def update(self, entry, cid):
        data, table = entry
        data["id"] = cid
        return entry
