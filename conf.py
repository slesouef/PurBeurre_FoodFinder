#! usr/bin/env python3
#! -*- coding:utf-8 -*-
"""file containing the configuration information for the application"""

# mySQL serveur configuration
USER = 'test'
PASSWORD = 'test'
SERVEUR = 'localhost'
DBNAME = 'test'

# API call configutation
URL = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&sort_by' \
      '=unique_scans_n&json=1'
PAGESIZE = 20

# MySQL database creation file location
SCRIPT = "data/creation_script.sql"
