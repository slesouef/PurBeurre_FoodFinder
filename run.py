#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""main application file. Contains main loop."""
from myrequest import *
from myconnector import *
from product import *
from categories import *
from history import *

from conf import *

def main_loop():

    # connect to database
    db = Database()

    # check database content
    # check = db.check_database()
    # if not check :
        # create tables
        # db.create_tables(SCRIPT)
    # else:
    #     print("tables ok")
    #     print(check)

    # DB CRUD
    table = Table(db)
    # product = Product("'evian'", "'150ml'", "'evian'", "'eau minerale'",
    #                   "'http://test.off.org'", "'a'", 1, 4)
    # entry = product.create()
    # pid = table.insert(entry)
    # entry = product.update(entry, pid)
    # update = table.update(entry, id=4)
    # read = table.read(entry, id=3)
    # delete = table.delete(entry, id=4)
    # print(update)

    # category = Category("'cola'", None)
    # entry = category.create()
    # cid = table.insert(entry)
    # entry = category.update(entry, cid)
    # read = table.read(entry, id=2)
    # cid = table.update(entry, id=1)
    # cid = table.delete(entry, id=3)
    # print(cid)

    # history = History(1, 2)
    # entry = history.create(history)
    # id =table.insert(entry)
    # read = table.read(entry, searched_pid=1)
    # delete = table.delete(entry, searched_pid=1)
    # print(delete)

    # call API to retrieve data
    # call = Call()
    # url = call.create_url()
    # call.api_request(url)

    # print("1 - Quel aliment souhaitez-vous remplacer ?" + '\n' + "2 - "
    #                  "Retrouver mes aliments substitués.")
    # choice = input("Votre choix:")
    # if choice == '1':
    #     print("categorie list")
    # elif choice == '2':
    #     print("saved list")
    # else:
    #     print("merci de bien vouloir fournir une valeur valide")


if __name__ == "__main__":
    main_loop()
