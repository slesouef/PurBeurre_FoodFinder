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
        try:
            connection = pymysql.connect(host=self.host,
                                     user=self.user,
                                     password=self.password,
                                     database=self.dbname)
            return connection
        except pymysql.err.InternalError:
             print('The database does not exist. Please check the '
                   'configuration.')

    def check_database(self, connection):
        """verify the database has been created"""
        cursor = connection.cursor()
        db_check = 'SHOW TABLES'
        cursor.execute(db_check)
        result = cursor.fetchall()
        return result

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
