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

    def create(self, connection, table_name, **data):
        """create entries in database"""
        # insert
        cursor = connection.cursor()  # initiate cursor
        # create insert statement:
        # INSERT INTO table_name (column1, column2, column3, ...)
        # VALUES (value1, value2, value3, ...);
        column = [a for a in data]
        values = [data[a] for a in data]
        where_insert = "INSERT INTO {} {}".format(table_name, tuple(column))
        clean_insert = where_insert.replace("'", "")
        insert = clean_insert + " VALUES {};".format(tuple(values))
        cursor.execute(insert)  # execute request
        connection.commit()
        # print(insert)

    def read(self, connection, table_name, *column_name, **conditions):
        """read entries in database"""
        # select
        cursor = connection.cursor()  # initiate cursor
        # create select statement
        # SELECT column1, column2, ...
        # FROM table_name
        # WHERE condition;
        column_list=[c for c in column_name]
        separator = ", "
        column = separator.join(column_list)
        select_what = "SELECT " + column
        select_where = select_what + " FROM {}".format(table_name)
        if len(conditions) != 0:
            while len(conditions) > 0:
                keys = []
                keys += conditions.popitem()
            condition_string = "{}={}".format(keys[0], keys[1])
            select = select_where + " WHERE {}".format(condition_string)
        else:
            select = select_where
        cursor.execute(select)  # execute request
        result = cursor.fetchall()
        return result
        # print(select_how)

    def update(self, connection, table_name, *data,
               **conditions):
        """update entries in database"""
        # update
        cursor = connection.cursor()  # initiate cursor
        # create update statement
        # UPDATE table_name
        # SET column1 = value1, column2 = value2, ...
        # WHERE condition;
        update_where = "UPDATE {}".format(table_name)
        values = [a for a in data]
        separator = ", "
        updates = separator.join(values)
        update_what = update_where + " SET {}".format(updates)
        while len(conditions) > 0:
            keys = []
            keys += conditions.popitem()
        condition_string = "{}={}".format(keys[0], keys[1])
        update = update_what + " WHERE {}".format(condition_string)
        cursor.execute(update)  # execute request
        connection.commit()
        # print(update)

    def delete(self, connection, table_name, **conditions):
        """delete entries in database"""
        # delete
        cursor = connection.cursor()  # initiate cursor
        # create delete statement
        # DELETE FROM table_name
        # WHERE condition;
        delete = "statement"
        cursor.execute(delete)  # execute request
