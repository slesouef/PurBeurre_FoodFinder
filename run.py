#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""main application file. Contains main loop."""
# from myrequest import *
from myconnector import *
# from product import *
from categories import *

from conf import *

def main_loop():

    # connect to database
    db = Database()

    # check database content
    check = db.check_database()
    if not check :
        # create tables
        db.create_tables(SCRIPT)
    else:
        print(check)

    # DB CRUD
    table = Table(db)

    # product entity
    product = Product("'evian'", "'1L'", "'evian'", "'eau minerale'",
                      "'http://test.off.org'", "'a'", 1, None)
    entry = product.create()
    pid = table.save(entry)
    entry = product.update(entry, pid)
    # update = table.save(entry)
    # read = table.read(entry)
    # delete = table.delete(entry)
    print(entry)

    # category entity
    category = Category("'beurre'", None)
    entry = category.create()
    cid = table.save(entry)
    entry = category.update(entry, cid)
    print(entry)

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
