#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""filtering of data from request in order to extract categories and products"""
import re

from conf import PAGESIZE, MIN_SIZE


class Filter:

    def __init__(self, data):
        # initialise data
        self.data = data
        # initialise result type
        self.categories = []

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
            if value > MIN_SIZE:
                self.categories.append(name.strip())
        # remove keys starting with 'xx:'
        pattern = re.compile('^..:')
        for i in self.categories:
            if pattern.match(i):
                # print(i)
                self.categories.remove(i)
        # return list of extracted categories
        return self.categories
        # print(self.data)

    def extract_products(self):
        """extract products from response data and insert them in DB"""
        # parse response to extract products for each category
        # return list of products by category
        pass
