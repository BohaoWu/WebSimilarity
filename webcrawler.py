# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webcrawler.py
@Time    :2020/3/24 19:18
"""

import requests


class Crawler:

    def __init__(self):
        self.websites = []

    def add_website(self, website):
        self.websites.append(website)
        return

    def crawler(self):
        return 1