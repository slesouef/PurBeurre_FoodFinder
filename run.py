#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""main application file. Contains main loop."""
from myrequest import *


def main_loop():
    call = Call()
    url = call.create_url()
    call.api_request(url)
    print(call.data)
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
