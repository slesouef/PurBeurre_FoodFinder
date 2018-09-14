#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""main controller for the application"""
from myconnector import *
from categories import *
from product import *


class Controller:
    """receives inputs and updates application screen"""

    def __init__(self):
        # open database connection
        self.db = Database()
        # initiate ORM
        self.table = Table(self.db)
        # setup navigation
        self.close = 0

    def landing(self):
        """display application landing page"""
        print(
            "1 - Trouver un substitut pour un aliment" + '\n' +
            "2 - Retrouver mes aliments substitués.")
        choice = input("Votre choix:")
        if choice == "1":
            self.show_categories()
        elif choice == "2":
            self.show_history()
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        else:
            print("merci de bien vouloir fournir une valeur valide")

    def show_categories(self):
        """displays a list of all categories in database.
           one categories can be selected."""
        print("Laquelle de ces categories vous interesse?")
        # select all categories from database
        category = Category()
        category = category.create()
        read = self.table.read(category)
        # create list of categories
        row = 1
        lookup = {}
        for i in read:
            # create display string
            name = i["name"]
            cat = str(row) + " - " + name
            # display category
            print(cat)
            # update lookup table
            lookup[str(row)] = name
            # update row id
            row += 1
        # wait for input
        choice = input("Votre choix:")
        # select category from input
        if choice in lookup:
            cid = [x["cid"] for x in read if x["name"] == lookup[choice]]
            cid = cid[0]
            self.show_products(cid)
        # close app
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        # display error
        else:
            print("merci de bien vouloir fournir une valeur valide")
            self.show_categories()

    def show_products(self, cid):
        """displays a list of all the products within a categorie.
           one product can be selected."""
        # select all product for the category selected
        product = Product()
        product = product.create()
        read = self.table.read(product, cid=cid)
        # read all database response
        row = 1
        lookup = {}
        for i in read:
            # create display string
            name = i["name"]
            quantity = i["quantity"]
            prod = str(row) + " - " + name + ", " + quantity
            # display category
            print(prod)
            # update lookup table
            lookup[str(row)] = i["pid"]
            # update row id
            row += 1
            # wait for input
        choice = input("Votre choix:")
        # identify product from input
        if choice in lookup:
            pid = [x["pid"] for x in read if x["pid"] == lookup[choice]]
            pid = pid[0]
            self.show_substitution(pid)
        # close app
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        # display error
        else:
            print("merci de bien vouloir fournir une valeur valide")
            self.show_products(cid)

    def show_substitution(self, pid):
        """displays the selected product and a substitution (lower rating)"""
        print(pid)

    def save_substition(self):
        """saves the selected product and its substitution in database"""
        pass

    def show_history(self):
        """displays the content of the history table"""
        print("history")
