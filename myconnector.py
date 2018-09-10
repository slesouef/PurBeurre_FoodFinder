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
        cursor = self.connection.cursor()  # initiate cursor
        # check if table exist
        cursor.execute('SHOW TABLES')
        result = cursor.fetchall()
        return result

    def create_tables(self, file):
        """create database from script"""
        cursor = self.connection.cursor()
        # open script
        with open(file, "r") as fd:
            # execute script
            for line in fd:
                cursor.execute(line)
        # close file
        fd.close()
        # commit changes
        self.connection.commit()


class Table:
    """interact with the content of the database"""

    def __init__(self, database):
        # initiate connection
        self.connection = database.connection

    def insert(self, entry):
        """modify the content of the database"""
        cursor = self.connection.cursor()  # initiate cursor
        # extract information from object data dictionary
        d_values, d_table = entry
        # create insert statement:
        # INSERT INTO table_name (column1, column2, column3, ...)
        # VALUES ('value1', 'value2', 'value3', ...);
        c_list = [str(x) for x in d_values if x != 'id']
        v_list = [str(d_values.get(x)) for x in d_values if x != 'id']
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
        r_id = cursor.lastrowid
        return r_id

    def update(self, entry, **condition):
        cursor = self.connection.cursor() # initiate cursor
        # exctract information form entry object
        d_values, d_table = entry
        # create update statement
        # UPDATE table_name
        # SET column1 = value1, column2 = value2, ...
        # WHERE condition;
        v_list = ["{}={}".format(x, d_values.get(x))
                  for x in d_values if x != 'id']
        separator = ", "
        values = separator.join(v_list)
        # create selector
        # check condition exists
        if not condition:
            # create update string with no where condition
            update = "UPDATE {} SET {};".format(d_table, values)
        else:
            # create selector string
            selector = ["{}={}".format(x, condition.get(x)) for x in condition]
            concat = " and "
            row = concat.join(selector)
            # create request string
            update = "UPDATE {} SET {} WHERE {};".format(d_table, values, row)
        # execute request
        cursor.execute(update)
        self.connection.commit()
        # return id
        r_id = cursor.lastrowid
        return r_id

    def read(self, entry, **condition):
        """read entries in database"""
        cursor = self.connection.cursor()  # initiate cursor
        # create select statement:
        # SELECT column1, column2, ...
        # FROM table_name
        # WHERE condition;
        d_values, d_table = entry
        # create string from columns list
        c_list = [str(x) for x in d_values]
        separator = ", "
        column = separator.join(c_list)
        # create condition string
        # check if conditions exist
        if not condition:
            # no condition, create select request with no where
            select = "SELECT {} FROM {};".format(column, d_table)
        else:
            # if condition, add where to select
            selector = ["{}={}".format(x, condition.get(x)) for x in condition]
            concat = ' and '
            row = concat.join(selector)
            # create request string
            select = "SELECT {} FROM {} WHERE {};".format(column, d_table, row)
        # execute request
        cursor.execute(select)
        # retrieve response
        reply = cursor.fetchall()
        extract = list(reply)
        # insert responses in list
        i = 0
        result = []
        while i < len(extract):
            # create dictionary entry per row returned
            single_row = dict(zip(c_list, extract[i]))
            i += 1
            result.append(single_row)
        return result

    def delete(self, entry, **condition):
        """delete entries in database"""
        cursor = self.connection.cursor()  # initiate cursor
        # create delete statement
        # DELETE FROM table_name
        # WHERE condition;
        d_values, d_table = entry
        # create condition string
        selector = ["{}={}".format(x, condition.get(x)) for x in condition]
        concat = ' and '
        row = concat.join(selector)
        # create request
        delete = "DELETE FROM {} WHERE {};".format(d_table, row)
        # execute request
        cursor.execute(delete)
        self.connection.commit()
        # return id
        r_id = cursor.lastrowid
        return r_id
