#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""contains method to interact with the MySQL database"""
import pymysql

from conf import *


class Database:
    """Connect and create database"""

    def __init__(self):
        # initiate user access
        self.user = USER
        self.password = PASSWORD
        # initiate database location
        self.host = SERVEUR
        # initiate database
        self.dbname = DBNAME
        # initiate connection
        self.connection = self.__connect()

    def __connect(self):
        """connect to the database"""
        try:
            connection = pymysql.connect(host=self.host,
                                         user=self.user,
                                         password=self.password,
                                         database=self.dbname)
            return connection
        except pymysql.err.InternalError:
            print(
                'The database does not exist. Please check the configuration.')

    def check_database(self):
        """verify the database has been created"""
        cursor = self.connection.cursor()
        db_check = 'SHOW TABLES'
        cursor.execute(db_check)
        result = cursor.fetchall()
        return result

    def create_db(self, file):
        """create database from script"""


class Table:
    """interact with the content of the database"""

    def __init__(self, database):
        # initiate connection
        self.connection = database.connection

    def save(self, entry):
        """modify the content of the database"""
        cursor = self.connection.cursor()  # initiate cursor
        # extract information from object data dictionary
        d_values, d_table = entry
        if d_values['id'] is None:
            # create insert statement:
            # INSERT INTO table_name (column1, column2, column3, ...)
            # VALUES ('value1', 'value2', 'value3', ...);
            c_list = [x for x in d_values if x != 'id']
            v_list = [d_values.get(x) for x in d_values if x != 'id']
            separator = ", "
            columns = separator.join(c_list)
            values = separator.join(v_list)
            # create request string
            insert = "INSERT INTO {} ({}) VALUES ({});".format(d_table, columns,
                                                               values)
            # execute request
            cursor.execute(insert)
            self.connection.commit()
            # return id
            id = cursor.lastrowid
            return id
        else:
            # create update statement
            # UPDATE table_name
            # SET column1 = value1, column2 = value2, ...
            # WHERE condition;
            v_list = ["{}={}".format(x, d_values.get(x)) for x in d_values if x != 'id']
            separator = ", "
            values = separator.join(v_list)
            row = d_values.get('id')
            # create request string
            update = "UPDATE {} SET {} d_table id={};".format(d_table, values, row)
            # execute request
            cursor.execute(update)
            self.connection.commit()

    def read(self, entry):
        """read entries in database"""
        cursor = self.connection.cursor()  # initiate cursor
        # create select statement:
        # SELECT column1, column2, ...
        # FROM table_name
        # WHERE condition;
        d_values, d_table = entry
        # create string from columns list
        c_list = [x for x in d_values]
        separator = ", "
        column = separator.join(c_list)
        row = "id={}".format(d_values['id'])
        # insert columns in SQL request string
        request = "SELECT {} FROM {} WHERE {};".format(column, d_table, row)
        # execute request
        cursor.execute(request)
        reply = cursor.fetchall()
        extract,  = reply
        data = list(extract)
        # result[*c_list] = *data
        # return result
        print(result)
        print(c_list)
        print(*c_list)
        print(*data)

    def delete(self, entry):
        """delete entries in database"""
        cursor = self.connection.cursor()  # initiate cursor
        # create delete statement
        # DELETE FROM table_name
        # WHERE condition;
        d_values, d_table = entry
        row = "id={}".format(d_values['id'])
        # create request
        request= "DELETE FROM {} WHERE {};".format(d_table, row)
        # execute request
        cursor.execute(request)
        self.connection.commit()
