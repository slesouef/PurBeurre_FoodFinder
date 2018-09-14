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
        read = table.read(category)
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
        # act on input
        if choice in lookup:
            for x in read:
                if x["name"] == lookup[choice]:
                    cid = x["cid"]
            self.show_products(cid)
        # close app
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        # display error
        else:
            print("merci de bien vouloir fournir une valeur valide")

    def show_products(self, cid):
        """displays a list of all the products within a categorie.
           one product can be selected."""
        print("products!!!")

    def show_substitution(self):
        """displays the selected product and a substitution (lower rating)"""
        pass

    def save_substition(self):
        """saves the selected product and its substitution in database"""
        pass

    def show_history(self):
        """displays the content of the history table"""
        print("history")
