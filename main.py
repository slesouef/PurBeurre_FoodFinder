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
            self.show_substitution(cid, pid)
        # close app
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        # display error
        else:
            print("merci de bien vouloir fournir une valeur valide")
            self.show_products(cid)

    def show_substitution(self, cid, pid):
        """displays the selected product and a substitution (lower rating)"""
        # retrieve product information
        product = Product()
        product = product.create()
        read = self.table.read(product, pid=pid)
        # read database response
        name = read[0]["name"]
        brand = read[0]["brand"]
        quantity = read[0]["quantity"]
        description = read[0]["description"]
        url = read[0]["url"]
        rating = read[0]["rating"]
        prod = "nom du produit: " + name + "\n" +\
               "marque du produit: " + brand + "\n" +\
               "quantite du produit: " + quantity + "\n" +\
               "description: " + description + "\n" +\
               "url: " + url + "\n" +\
               "rating: " + rating
        print(prod)
        read = self.table.read(product, cid=cid)
        rating_list = {x["pid"]: x["rating"] for x in read}
        sub_pid = sorted(rating_list, key=rating_list.get)
        sub_pid = sub_pid[0]
        read = self.table.read(product, pid=sub_pid)
        # read database response
        sub_name = read[0]["name"]
        sub_brand = read[0]["brand"]
        sub_quantity = read[0]["quantity"]
        sub_description = read[0]["description"]
        sub_url = read[0]["url"]
        sub_rating = read[0]["rating"]
        sub = "nom du produit: " + sub_name + "\n" + \
               "marque du produit: " + sub_brand + "\n" + \
               "quantite du produit: " + sub_quantity + "\n" + \
               "description: " + sub_description + "\n" + \
               "url: " + sub_url + "\n" + \
               "rating: " + sub_rating
        print(sub)
        # propose to save this search
        choice = input("voulez vous sauvegarder cette recherche (Oui/Non)?")
        # user wants to save this search
        if choice.lower() == "oui" or choice.lower() == "o":
            self.save_substitution(pid, sub_pid)
        # user does not save this search
        elif choice.lower() == "non" or choice.lower() == "n":
            self.landing()
        # close app
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        # display error
        else:
            print("merci de bien vouloir fournir une valeur valide")
            self.show_substitution(cid, pid)

    def save_substitution(self, pid, sub_pid):
        """saves the selected product and its substitution in database"""
        pass

    def show_history(self):
        """displays the content of the history table"""
        print("history")
