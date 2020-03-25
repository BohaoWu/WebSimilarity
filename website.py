# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :website.py
@Time    :2020/3/25 16:18
"""

from bs4 import BeautifulSoup
import bs4


class Website:

    def __init__(self, url, soup: BeautifulSoup, loc='', topic=False, relevance=0):
        self.url = url
        self.soup = soup
        self.loc = loc
        self.topic = topic
        self.relevance = relevance

    def get_text(self):
        return self.soup.text

    def get_dom_tree(self):
        for content in self.soup.contents:
            if isinstance(content, bs4.element.Tag):
                continue
        return self.soup
