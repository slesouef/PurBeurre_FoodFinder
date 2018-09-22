#! usr/env/bin python3
# -*- coding:utf-8 -*-
"""run the application"""
from launch import *
from main import *


def main():

    launch = Launch()
    if launch.check_db() and launch.check_tables() and launch.check_content():
        app = Controller()
        while app.close == 0:
            app.landing()
    else:
        print("La base de données est mal configurée. Merci de verifier"
              " votre configuration.")


if __name__ == "__main__":
    main()
