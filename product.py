#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Manipulate product objects"""
from conf import *


class Product:

    def __init__(self, name, quantity, id=None):
        # data format
        self.db_format = {"name": "name", "quantity": "quantity", "id": "id"}
        # initialise data
        self.name = name
        self.quantity = quantity
        self.id = id
        # initialise table
        self.table = PRODUCT

    def create_object(self):
        values = self.db_format
        values["name"] = self.name
        values["quantity"] = self.quantity
        values["id"] = self.id
        table_name = self.table
        return values, table_name

    def update_object(self, object, id):
        data = list(object)
        value = data[0]
        value["id"] = str(id)
        return object