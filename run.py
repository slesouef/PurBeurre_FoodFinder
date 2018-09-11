#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""run the application"""
from launch import *


def main():

    launch = Launch()
    launch.check_db()
    if launch.DB_ok is True:
        launch.check_tables()
        if launch.tables_ok is True:
            launch.check_content()
            if launch.content_ok is True:
                print(
                    "1 - Quel aliment souhaitez-vous remplacer ?" + '\n' +
                    "2 - Retrouver mes aliments substitués."
                    )
                choice = input("Votre choix:")
                if choice == '1':
                    print("categorie list")
                elif choice == '2':
                    print("saved list")
                else:
                    print("merci de bien vouloir fournir une valeur valide")
            else:
                print("no content")
        else:
            print("no tables")
    else:
        print("The database does not exist. Please check the configuration.")


    # DB CRUD
    # table = Table(db)
    # product = Product("'evian'", "'150ml'", "'evian'", "'eau minerale'",
    #                   "'http://test.off.org'", "'a'", 1, 4)
    # entry = product.create()
    # pid = table.insert(entry)
    # entry = product.update(entry, pid)
    # update = table.update(entry, id=4)
    # read = table.read(entry, id=3)
    # delete = table.delete(entry, id=4)
    # print(update)

    # category = Category("'test3'", None)
    # entry = category.create()
    # cid = table.insert(entry)
    # entry = category.update(entry, cid)
    # read = table.read(entry, id=1)
    # cid = table.update(entry)
    # cid = table.delete(entry, id=3)
    # print(cid)

    # history = History(1, 2)
    # entry = history.create(history)
    # id =table.insert(entry)
    # read = table.read(entry, searched_pid=1)
    # delete = table.delete(entry, searched_pid=1)
    # print(delete)


if __name__ == "__main__":
    main()
