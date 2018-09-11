#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""launch checks"""
from myconnector import *
from myrequest import *
from filter import *

from conf import SCRIPT


class Launch:
    """class to verify the application is in a usable state
       methods return True if OK"""

    def check_db(self):
        # connect to database
        try:
            Database()
            return True
        # connection error
        except pymysql.err.InternalError:
            return False

    def check_tables(self):
        # connect to database
        db = Database()
        # check tables
        check = db.check_database()
        if not check:
            try:
                # create tables
                db.create_tables(SCRIPT)
                return True
            except pymysql.err.ProgrammingError:
                return False
        else:
            return True

    def check_content(self):
        # connect to database
        db = Database()
        # initiate orm
        table = Table(db)
        # initiate tables
        category = Category()
        product = Product()
        # check for content
        category = category.create()
        product = product.create()
        select_category = table.read(category)
        select_product = table.read(product)
        if not select_category and not select_product:
            # call API to retrieve data
            call = Call()
            url = call.create_url()
            data = call.api_request(url)
            # data treatment
            screen = Filter(data.data)
            screen.extract_categories()
            screen.insert_categories(table)
            screen.extract_products()
            screen.insert_product(table)
            return True
        elif not select_product:
            # call API to retrieve data
            call = Call()
            url = call.create_url()
            data = call.api_request(url)
            # data treatment
            screen = Filter(data.data)
            screen.extract_categories()
            screen.extract_products()
            screen.insert_product(table)
            return True
        else:
            return True
