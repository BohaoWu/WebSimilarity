# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webparser.py
@Time    :2020/3/24 14:08
"""

import bs4
from bs4 import BeautifulSoup


class WebParser:

    def __init__(self, html):
        self.id = 0
        self.html = html
        self.soups = BeautifulSoup(self.html, 'lxml')

    def get_text(self):
        return self.html.text

    def get_dom_tree(self):
        for content in self.soups.contents:
            if isinstance(content, bs4.element.Tag):
                continue
        return self.html
