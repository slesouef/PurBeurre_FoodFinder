#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""filtering of data from request in order to extract categories and products"""
import re

from categories import *
from product import *
from pymysql.err import ProgrammingError

from conf import PAGESIZE, MIN_SIZE


class Filter:

    def __init__(self, data):
        # initialise data
        self.data = data
        # initialise result type
        self.categories = []
        self.products = []

    def extract_categories(self):
        """extract categories from response data and insert them in DB"""
        # parse response to extract categories w/count into a dictionary
        i = 0
        count = {}
        while i < PAGESIZE:
            # add catgories in a dictionary to count how any elements per
            a = self.data["products"][i]["categories"].split(",")
            b = a[-1]
            if b not in count:
                count[b] = 1
            else:
                count[b] += 1
            i += 1
        # extract from dictionary categories with MIN_SIZE < x products
        for name, value in count.items():
            if value >= MIN_SIZE:
                self.categories.append(name.strip())
        # remove keys starting with 'xx:'
        pattern = re.compile('^..:')
        # print(self.categories)
        # print(len(self.categories))
        for i in self.categories:
            # print(i)
            if pattern.match(i):
                # print(i)
                self.categories.remove(i)
        # return list of extracted categories
        return self.categories

    def extract_products(self):
        """extract products from response data and insert them in DB"""
        # parse response to extract products for each category
        i = 0
        while i < PAGESIZE:
            # get category name from data
            a = self.data["products"][i]["categories"].split(",")
            b = a[-1]
            # check category is in category list
            if b in set(self.categories):
                # if a product element missing, disregard entry
                try:
                    # initialise product entry
                    product = {}
                    # add name
                    name = self.data["products"][i]["product_name_fr"]
                    name = "'" + name + "'"
                    product["name"] = name
                    # add quantity
                    quantity = self.data["products"][i]["quantity"]
                    quantity = "'" + quantity + "'"
                    product["quantity"] = quantity
                    # add brand
                    brand = self.data["products"][i]["brands"]
                    brand = "'" + brand + "'"
                    product["brand"] = brand
                    # add description
                    description = self.data["products"][i]["generic_name_fr"]
                    description = "'" + description + "'"
                    product["description"] = description
                    # add url
                    url = self.data["products"][i]["url"]
                    url = "'" + url + "'"
                    product["url"] = url
                    # add rating
                    rating = self.data["products"][i]["nutrition_grade_fr"]
                    rating = "'" + rating + "'"
                    product["rating"] = rating
                    # add category
                    product["category"] = b
                    # append product dictionary element to products list
                    self.products.append(product)
                except KeyError:
                    pass
                finally:
                    i += 1
            else:
                i += 1
        # return list of products by category
        return self.products

    def insert_categories(self, table):
        for i in self.categories:
            # extract data
            name = "'" + str(i) + "'"
            # create category object
            category = Category(name)
            category = category.create()
            # insert in database
            try:
                table.insert(category)
            except ProgrammingError:
                pass

    def insert_product(self, table):
        for i in self.products:
            # extract data
            name = i["name"]
            quantity = i["quantity"]
            brand = i["brand"]
            description = i["description"]
            url = i["url"]
            rating = i["rating"]
            category = i["category"]
            # get cid from category name
            cat = Category(category)
            cat = cat.create()
            arg = '"' + category + '"'
            cid = table.read(cat, name=arg)
            cid = cid[0]
            cid = cid["cid"]
            # create product object
            product = Product(name, quantity, brand, description, url,
                              rating, cid)
            product = product.create()
            # insert in database
            try:
                table.insert(product)
            except ProgrammingError:
                pass
