#! usr/bin/env python3
#! -*- coding:utf-8 -*-
"""contains method to interact with the MySQL database"""
import pymysql

from conf import *


class Database:
    """Connect and create database"""

    def __init__(self):
        #initiate user access
        self.user = USER
        self.password = PASSWORD
        #initiate database location
        self.host = SERVEUR
        #initiate database
        self.dbname = DBNAME

    def connect(self):
        """connect to the database"""
        connection = pymysql.connect(host='self.host', port='self.port',
                                     user='self.user',
                                     password='self.password',
                                     database='self.db')
        return connection

    def check_database(self, connection):
        """verify the database has been created"""

    def create_db(self, file):
        """create database from script"""

class Table:
    """interact with the content of the database"""

    def search_category(self):
        """search for categories"""

    def search_product(self):
        """search foa products in a category"""

    def search_substitute(self):
        """search for a substitute product"""

    def save_search(self):
        """insert search results in history"""
