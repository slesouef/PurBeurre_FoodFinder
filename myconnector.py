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
            print('The database does not exist. Please check the '
                   'configuration.')

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

    def create(self, object):
        """create entries in database"""
        cursor = self.connection.cursor()  # initiate cursor
        # extract information from object data dictionary
        data = list(object)
        what = data[0]
        where = data[1]
        if what['id'] == None:
            # create insert statement:
            # INSERT INTO table_name (column1, column2, column3, ...)
            # VALUES ('value1', 'value2', 'value3', ...);
            c_list = [x for x in what if x != 'id']
            separator = ", "
            columns = separator.join(c_list)
            v_list = [what.get(x) for x in what if x != 'id']
            values = separator.join(v_list)
            # create request string
            insert = "INSERT INTO {} ({}) VALUES ({});".format(where, columns,
                                                              values)
            # execute request
            cursor.execute(insert)
            self.connection.commit()
            # return id
            id = cursor.lastrowid
            return id
        else:
            pass

    def read(self, connection, table_name, *column_name, **conditions):
        """read entries in database"""
        cursor = connection.cursor()  # initiate cursor
        # create select statement:
        # SELECT column1, column2, ...
        # FROM table_name
        # WHERE condition;
        # create string from columns list
        column_list = [c for c in column_name]
        separator = ", "
        column = separator.join(column_list)
        # insert columns in SQL request string
        select_what = "SELECT " + column
        # add target table to SQL request string
        select_where = select_what + " FROM {}".format(table_name)
        # check if conditions exist
        if len(conditions) != 0:
            # extract condition from dictonary
            while len(conditions) > 0:
                keys = []
                keys += conditions.popitem()
            # add condition values to a string
            condition_string = "{}={}".format(keys[0], keys[1])
            # add conditions to SQL request string
            select = select_where + " WHERE {}".format(condition_string)
        else:
            select = select_where
        # execute request
        cursor.execute(select)
        result = cursor.fetchall()
        return result

    def update(self, connection, table_name, *data,
               **conditions):
        """update entries in database"""
        cursor = connection.cursor()  # initiate cursor
        # create update statement
        # UPDATE table_name
        # SET column1 = value1, column2 = value2, ...
        # WHERE condition;
        # add target table to SQL request string
        update_where = "UPDATE {}".format(table_name)
        # create string from data list
        values = [a for a in data]
        separator = ", "
        updates = separator.join(values)
        # add values to SQL request
        update_what = update_where + " SET {}".format(updates)
        # extract condition from dictionary
        while len(conditions) > 0:
            keys = []
            keys += conditions.popitem()
        # add condition to string
        condition_string = "{}={}".format(keys[0], keys[1])
        # update SQL request with condition
        update = update_what + " WHERE {}".format(condition_string)
        # execute request
        cursor.execute(update)
        connection.commit()

    def delete(self, connection, table_name, **conditions):
        """delete entries in database"""
        cursor = connection.cursor()  # initiate cursor
        # create delete statement
        # DELETE FROM table_name
        # WHERE condition;
        # add target table to SQL request string
        delete_where = "DELETE FROM {}".format(table_name)
        # extract condition from dictionary
        while len(conditions) > 0:
            keys = []
            keys += conditions.popitem()
        # add condition to string
        condition_string = "{}={}".format(keys[0], keys[1])
        # update SQL request
        delete = delete_where + " WHERE {}".format(condition_string)
        # execute request
        cursor.execute(delete)
        connection.commit()
