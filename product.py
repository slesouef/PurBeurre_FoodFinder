#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""product entity"""
from conf import *


class Product:

    def __init__(self, name, quantity, brand, description, url, rating,
                 category_id, pid=None):
        # data format
        self.db_format = {
            "name": "name", "quantity": "quantity", "brand": "brand",
            "description": "description", "url": "url", "rating": "rating",
            "category_id": "category_id", "id": "id"}
        # initialise data
        self.name = name
        self.quantity = quantity
        self.brand = brand
        self.description = description
        self.url = url
        self.rating = rating
        self.category_id = category_id
        self.id = pid
        # initialise table
        self.table = PRODUCT

    def create(self):
        values = self.db_format
        values["name"] = self.name
        values["quantity"] = self.quantity
        values["brand"] = self.brand
        values["description"] = self.description
        values["url"] = self.url
        values["rating"] = self.rating
        values["category_id"] = self.category_id
        values["id"] = self.id
        table_name = self.table
        return values, table_name

    def update(self, entry, pid):
        data, table = entry
        data["id"] = pid
        return entry
