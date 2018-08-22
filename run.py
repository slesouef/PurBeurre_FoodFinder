#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""main application file. Contains main loop."""
# from myrequest import *
from myconnector import *


def main_loop():

    # connect to database
    db = Database()
    connection = db.connect()

    # check database content
    # check = db.check_database(connection)
    # print (check)

    # create info in database
    # table = Table()
    # table.create(connection, "test", name="briquets", quantity=100)

    # read info in database
    # table = Table()
    # select = table.read(connection, "test", "*")
    # print(select)

    # update info in database
    # table = Table()
    # table.update(connection, "test", "name='jouet'", "quantity='24'", id=4)

    # delete info in database
    table = Table()
    table.delete(connection, "test", id=1)

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
