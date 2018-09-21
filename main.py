#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""main controller for the application"""
from myconnector import *
from categories import *
from product import *
from history import *

from pymysql.err import IntegrityError


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
            "Bienvenue dans l'application FoodFinder." + "\n" +
            "Merci de sélectionner le numéro de l'action que vous souhaitez "
            "accomplir:" + "\n" +
            "1 - Trouver un substitut pour un aliment" + "\n" +
            "2 - Retrouver mes aliments substitués" + "\n" +
            "Vous pouvez quitter l’application à tout moment en écrivant exit "
            "dans le champ de sélection.")
        choice = input("Votre choix:")
        if choice == "1":
            self.show_categories()
        elif choice == "2":
            self.show_history()
        elif choice == "exit":
            self.db.connection.close()
            self.close = 1
        else:
            print("Merci de bien vouloir fournir une valeur valide")

    def show_categories(self):
        """displays a list of all categories in database.
           one categories can be selected."""
        print("Voici la liste des catégories disponible." + "\n" +
              "Choisissez le numéro de la catégorie qui vous intéresse.")
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
            print("Merci de bien vouloir fournir une valeur valide")
            self.show_categories()

    def show_products(self, cid):
        """displays a list of all the products within a categorie.
           one product can be selected."""
        # select all product for the category selected
        print("Voici la liste des produits disponible dans cette catégorie."
              + "\n" +
              "Merci de choisir le numéro du produit qui vous intéresse.")
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
            print("Merci de bien vouloir fournir une valeur valide")
            self.show_products(cid)

    def show_substitution(self, cid, pid):
        """displays the selected product and a substitution (lower rating)"""
        # retrieve product information
        print("Voici les informations du produit que vous avez choisi:")
        product = Product()
        product = product.create()
        prod_read = self.table.read(product, pid=pid)
        read = prod_read[0]
        # read database
        prod = "Nom du produit: " + read["name"] + "\n" + \
               "Marque du produit: " + read["brand"] + "\n" + \
               "Quantité du produit: " + read["quantity"] + "\n" + \
               "Description: " + read["description"] + "\n" + \
               "url: " + read["url"] + "\n" + \
               "Note nutri-score: " + read["rating"]
        print(prod + "\n" + "Voici un autre produit ayant une note supérieure "
                            "ou égale au produit que vous avez sélectionnez:")
        read = self.table.read(product, cid=cid)
        rating_list = {x["pid"]: x["rating"] for x in read}
        sub_pid = sorted(rating_list, key=rating_list.get)
        sub_pid = sub_pid[0]
        sub_read = self.table.read(product, pid=sub_pid)
        # read database response
        read = sub_read[0]
        sub = "Nom du produit: " + read["name"] + "\n" + \
              "Marque du produit: " + read["brand"] + "\n" + \
              "Quantité du produit: " + read["quantity"] + "\n" + \
              "Description: " + read["description"] + "\n" + \
              "url: " + read["url"] + "\n" + \
              "Note nutri-score: " + read["rating"]
        print(sub)
        # propose to save this search
        choice = input("Voulez vous sauvegarder cette recherche (Oui/Non)?")
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
            print("Merci de bien vouloir fournir une valeur valide")
            self.show_substitution(cid, pid)

    def save_substitution(self, pid, sub_pid):
        """saves the selected product and its substitution in database"""
        # case for previous choice was bad input
        if not pid and not sub_pid:
            choice = input(
                "Votre recherche a été sauvegardée. "
                "Voulez vous faire une autre recherche (Oui/Non)?")
            # user wants to do another search
            if choice.lower() == "oui" or choice.lower() == "o":
                self.landing()
            # user does not want to continue searching
            elif choice == "exit" or choice.lower() == "non" \
                    or choice.lower() == "n":
                self.db.connection.close()
                self.close = 1
            # display error
            else:
                print("Merci de bien vouloir fournir une valeur valide")
                self.save_substitution(None, None)
        # case from show_substitution
        else:
            # instantiate a history object with parameters from
            # show_substitution
            history = History(pid, sub_pid)
            history = history.create()
            # try an insert but catch the case where the save has already
            # been done
            try:
                self.table.insert(history)
                choice = input("Votre recherche a été sauvegardée. "
                               "Voulez vous faire une autre recherche "
                               "(Oui/Non)?")
            except IntegrityError:
                choice = input("Cette recherche a déjà été sauvegardée. "
                               "Voulez-vous faire une autre recherche "
                               "(Oui/Non)?")
            # user wants to do another search
            if choice.lower() == "oui" or choice.lower() == "o":
                self.landing()
            # user does not want to continue searching
            elif choice == "exit" or choice.lower() == "non" \
                    or choice.lower() == "n":
                self.db.connection.close()
                self.close = 1
            # display error
            else:
                print("Merci de bien vouloir fournir une valeur valide")
                self.save_substitution(None, None)

    def show_history(self):
        """displays the content of the history table"""
        # instanciate a history object
        history = History()
        history = history.create()
        read = self.table.read(history)
        for i in read:
            pid = i["pid"]
            sub_pid = i["sub_pid"]
            date = i["date"]
            # retrieve product information
            product = Product()
            product = product.create()
            table_read = self.table.read(product, pid=pid)
            prod_read = table_read[0]
            # read database response
            prod = "Nom du produit: " + prod_read["name"] + ", " + \
                   "Quantité du produit: " + prod_read["quantity"] + ", " + \
                   "Note nutri-score: " + prod_read["rating"]
            # retrieve substitution information
            table_read = self.table.read(product, pid=sub_pid)
            sub_read = table_read[0]
            # read database response
            sub = "Nom du produit: " + sub_read["name"] + ", " + \
                  "Quantité du produit: " + sub_read["quantity"] + ", " + \
                  "Note Nutri-score: " + sub_read["rating"]
            display = "Sauvegarde du " + str(date) + ":\n" + prod + "\n" + sub
            print(display)
