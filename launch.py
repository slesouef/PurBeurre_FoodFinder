#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""launch checks"""
from myconnector import *
from categories import *
from product import *
from myrequest import *
from filter import *

from conf import SCRIPT


class Launch:
    """class to verify the application is in a usable state"""

    def __init__(self):
        # initiate checks status
        self.DB_ok = False
        self.tables_ok = False
        self.content_ok = False

    def check_db(self):
        # connect to database
        try:
            db = Database()
            self.DB_ok = True
        # connection error
        except pymysql.err.InternalError:
            pass

    def check_tables(self):
        # connect to database
        db = Database()
        # check tables
        check = db.check_database()
        if not check:
            try:
                # create tables
                db.create_tables(SCRIPT)
                self.tables_ok = True
            except pymysql.err.ProgrammingError:
                pass
        else:
            self.tables_ok = True

    def check_content(self):
        # connect to database
        db = Database()
        # initiate orm
        table = Table(db)
        # initiate tables
        category = Category()
        product = Product()
        # check for content
        entry = product.create()
        select = table.read(entry)
        if not select:
            # call API to retrieve data
            call = Call()
            url = call.create_url()
            data = call.api_request(url)
            # data treatment
            screen = Filter(data.data)
            categories = screen.extract_categories()
            print(categories)
            print(len(categories))
            products = screen.extract_products()
            print(products)
            print(len(products))
        else:
            self.content_ok = True
