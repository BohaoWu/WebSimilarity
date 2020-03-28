# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webcrawler.py
@Time    :2020/3/24 19:18
"""

import requests
from bs4 import BeautifulSoup
import time

from website import Website
import webclassifier


class WebsiteNode:

    def __init__(self, website: Website):
        self.website = website
        self.child = []

    def add_child(self, website: Website):
        self.child.append(WebsiteNode(website))

class Crawler:

    def __init__(self, threshold=0.5):
        self.website_nodes = []
        self.root_node = None
        self.threshold = threshold

    def set_root_website(self, website:Website):
        self.root_node = WebsiteNode(website)
        self.website_nodes.append(WebsiteNode(website))
        return

    def crawler(self, classifier: webclassifier.Classifier):
        if len(self.website_nodes) == 0:
            print("There are no more websites need to be crawled.")
            return False

        new_website_nodes = []
        for website_node in self.website_nodes:
            for url in website_node.website.soup.find_all('a'):
                try:
                    url.attrs['href']
                except KeyError:
                    continue

                # Crawled website need not crawl again.
                if url.attrs['href'] in classifier.url:
                    print('This website has been added into classifier.')
                    continue

                # Decide which website can be stored
                try:
                    new_website_node = WebsiteNode(Website(url.attrs['href'], get_soup(url.attrs['href'])))
                except Exception:
                    print('Invalid url ', url['href'])
                else:
                    classifier.add_website(new_website_node.website)
                    classifier.cal()
                    new_website_node.website.relevance = -1
                    for seed in classifier.seed_websites:
                        rel = classifier.calculate_web_similarity_by_text(seed, new_website_node.website)
                        new_website_node.website.relevance = max(new_website_node.website.relevance, rel)
                    if new_website_node.website.relevance > self.threshold:
                        print(url.attrs['href'], 'is relative, relevance is %s' % new_website_node.website.relevance)
                        website_node.child.append(new_website_node)
                        new_website_nodes.append(new_website_node)

        classifier.cal()
        self.website_nodes = new_website_nodes
        return True


def get_soup(url):
    r = requests.get(url)
    r.encoding = 'utf-8'
    time.sleep(5)
    soup = BeautifulSoup(r.text, 'lxml')
    return soup
