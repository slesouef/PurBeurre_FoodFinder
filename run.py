#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""main application file. Contains main loop."""
import os
import requests
import json


def check_data():
    """load the data from open food facts in memory."""
    # check if json file exists
    try:
        data_file = open('data/dump.json', "r")
        data_file.close()
    # create json file if necessary
    except FileNotFoundError:
        r = requests.get('https://fr.openfoodfacts.org/cgi/search.pl?action='
                         'process&sort_by=unique_scans_n&page_size=1000&json=1')
        if r.status_code == 200:
            os.mkdir('data')
            data = r.json()
            with open('data/dump.json', "w") as fd:
                json.dump(data, fd)
            fd.close()
        else:
            print(r.raise_for_status())


def main_loop():
    check_data()
    print("1 - Quel aliment souhaitez-vous remplacer ?" + '\n' + "2 - "
                     "Retrouver mes aliments substitués.")
    choice = input("Votre choix:")
    if choice == '1':
        print("categorie list")
    elif choice == '2':
        print("saved list")
    else:
        print("merci de bien vouloir fournir une valeur valide")


if __name__ == "__main__":
    main_loop()
