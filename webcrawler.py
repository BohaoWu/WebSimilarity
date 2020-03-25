# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webcrawler.py
@Time    :2020/3/24 19:18
"""

import requests
from bs4 import BeautifulSoup
from website import Website
import webclassifier


class WebsiteNode:

    def __init__(self, website: Website):
        self.website = website
        self.child = []

    def add_child(self, website: Website):
        self.child.append(WebsiteNode(website))

class Crawler:

    def __init__(self, threshold = 0.5):
        self.website_nodes = []
        self.root_node = None
        self.threshold = threshold

    def set_root_website(self, website:Website):
        self.root_node = WebsiteNode(website)
        self.website_nodes.append(WebsiteNode(website))
        return

    def crawler(self):
        if len(self.website_nodes) == 0:
            print("There are no more websites need to be crawled.")
            return False
        new_website_nodes = []
        for website_node in self.websiteNodes:
            for url in website_node.website.soup.find_all('a'):
                new_website_node = WebsiteNode(Website(url, get_soup(url), relevance=1))
                if new_website_node.website.relevance > self.threshold:
                    website_node.child.append(new_website_node)
                    new_website_nodes.append(new_website_node)
        self.website_nodes = new_website_nodes
        return True


def get_soup(self, url):
    try:
        r = requests.get(url)
    except TimeoutError:
        print("Can't connect url.")
        return 0
    r.encoding('utf-8')
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
