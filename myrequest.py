#! usr/bin/env python3
# -*- coding:utf-8 -*-
"""Contains method to create and execute API request against Open Food Facts
server"""
import requests

from conf import *


class Call:
    """API call must be constructed from configuration"""

    def __init__(self):
        # initialize api request
        self.url = URL
        self.pagesize = PAGESIZE
        # initialize reponse object
        self.data = {}

    def create_url(self):
        """construct request URL"""
        call = '{}&pagesize={}'.format(self.url, self.pagesize)
        return call

    def api_request(self, url):
        """GET info from API and insert it into a dictionary object"""
        r = requests.get(url)
        self.data = r.json()