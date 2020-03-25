# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webclassifier.py
@Time    :2020/3/24 21:08
"""

import calsimilarity
from website import Website


class Classifier:

    def __init__(self, seed_websites, threshold=0.5):
        self.websites = []
        self.seed_websites = seed_websites
        self.threshold = threshold

    def set_seed_website(self, seed_websites):
        self.seed_websites = seed_websites

    def add_website(self, website:Website.Website):
        self.websites.append(website)
        self.cal()
        return

    def topic_classifier(self, website: Website.Website):
        for seed in self.seed_websites:
            if calsimilarity.calculate_web_similarity(website, seed) > self.threshold:
                return True
        return False

    def cal(self):
        return