#! usr/bin/env python3
#! -*- coding:utf-8 -*-
"""file containing the configuration information for the application"""

# mySQL serveur configuration
USER = 'test'
PASSWORD = 'test'
SERVEUR = 'localhost'
DBNAME = 'Test'

# API call configutation
URL = 'https://fr.openfoodfacts.org/cgi/search.pl?action=process&sort_by' \
      '=unique_scans_n&json=1'
PAGESIZE = 20
