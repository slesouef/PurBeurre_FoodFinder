#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""product entity"""
from conf import *


class Product:

    def __init__(self, name=None, quantity=None, brand=None, description=None,
                 url=None, rating=None, cid=None, pid=None):
        # data format
        self.db_format = {
            "name": "name", "quantity": "quantity", "brand": "brand",
            "description": "description", "url": "url", "rating": "rating",
            "cid": "cid", "pid": "pid"}
        # initialise data
        self.name = name
        self.quantity = quantity
        self.brand = brand
        self.description = description
        self.url = url
        self.rating = rating
        self.cid = cid
        self.pid = pid
        # initialise table
        self.table = PRODUCT

    def create(self):
        """return a tuple containing value dictionary and table name"""
        values = self.db_format
        values["name"] = self.name
        values["quantity"] = self.quantity
        values["brand"] = self.brand
        values["description"] = self.description
        values["url"] = self.url
        values["rating"] = self.rating
        values["cid"] = self.cid
        values["pid"] = self.pid
        table_name = self.table
        return values, table_name

    def update(self, entry, pid):
        """update object inserted in database with id"""
        data, table = entry
        data["pid"] = pid
        return entry
