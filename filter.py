#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""filtering of data from request in order to extract categories and
   products to be inserted in database
   """
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
        """extract categories from response data"""
        # parse response to extract categories w/count into a dictionary
        i = 0
        count = {}
        while i < PAGESIZE:
            # create count dictionary
            a = self.data["products"][i]["categories"].split(",")
            b = a[-1]
            if b not in count:
                count[b] = 1
            else:
                count[b] += 1
            i += 1
        # extract from dictionary categories with MIN_SIZE < x products
        cat_list = []
        for name, value in count.items():
            if value >= MIN_SIZE:
                name = name.strip()
                clean = name.replace("'", r"\'")  # escape apostrophe for sql
                cat_list.append(clean)
        # remove keys starting with 'en:' or 'fr:'
        pattern = re.compile('^..:')
        for i in cat_list:
            if not pattern.match(i):
                self.categories.append(i)
        # return list of extracted categories
        return self.categories

    def extract_products(self):
        """extract products from response data"""
        # parse response to extract products for each category
        i = 0
        while i < PAGESIZE:
            # get category name from data
            a = self.data["products"][i]["categories"].split(",")
            b = a[-1]
            # check category is in category list
            if b in set(self.categories):
                try:
                    # initialise product entry
                    product = {}
                    # add name
                    raw_name = self.data["products"][i]["product_name_fr"]
                    clean_name = raw_name.replace("'", r"\'")
                    name = "'" + clean_name + "'"
                    product["name"] = name
                    # add quantity
                    raw_quantity = self.data["products"][i]["quantity"]
                    quantity = "'" + raw_quantity + "'"
                    product["quantity"] = quantity
                    # add brand
                    raw_brand = self.data["products"][i]["brands"]
                    clean_brand = raw_brand.replace("'", r"\'")
                    brand = "'" + clean_brand + "'"
                    product["brand"] = brand
                    # add description
                    raw_description = self.data["products"][i][
                        "generic_name_fr"]
                    clean_description = raw_description.replace("'", r"\'")
                    description = "'" + clean_description + "'"
                    product["description"] = description
                    # add url
                    raw_url = self.data["products"][i]["url"]
                    url = "'" + raw_url + "'"
                    product["url"] = url
                    # add rating
                    raw_rating = self.data["products"][i]["nutrition_grade_fr"]
                    rating = "'" + raw_rating + "'"
                    product["rating"] = rating
                    # add category
                    product["category"] = b
                    # append product dictionary element to products list
                    self.products.append(product)
                # if a product element missing, disregard entry
                except KeyError:
                    pass
                finally:
                    i += 1
            else:
                i += 1
        # return list of products by category
        return self.products

    def insert_categories(self, table):
        """insert categories in database"""
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
                raise

    def insert_product(self, table):
        """insert products in database"""
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
                raise

    def clean_categories(self, table):
        """remove categories with no products"""
        # get list of categories in database
        cat = Category()
        cat = cat.create()
        cat_list = table.read(cat)
        # instantiate products table
        prod = Product()
        prod = prod.create()
        for i in cat_list:
            # check number of products for a category
            cid = i["cid"]
            check = table.read(prod, cid=cid)
            # delete category if empty
            if not check:
                table.delete(cat, cid=cid)
            else:
                pass
