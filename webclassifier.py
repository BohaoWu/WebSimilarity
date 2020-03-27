# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webclassifier.py
@Time    :2020/3/24 21:08
"""

from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from website import Website


class Classifier:
    """
    This class stores text of website. Calculate tf-idf for crawler.
    """

    def __init__(self, seed_websites, threshold=0.5):
        self.url = []
        self.websites = []
        self.corpus = []
        self.seed_websites = seed_websites
        self.websites.extend(seed_websites)
        for website in seed_websites:
            self.corpus.append(website.get_text())
        self.threshold = threshold
        self.words = []
        self.f = None
        self.tfidf = []

    def set_seed_website(self, seed_websites):
        self.seed_websites = seed_websites

    def add_website(self, website:Website.Website):
        self.url.append(website.url)
        self.websites.append(website)
        self.corpus.append(website.get_text())
        return

    def cal(self):
        vectorizer = CountVectorizer()
        f = vectorizer.fit_transform(self.corpus)
        word = vectorizer.get_feature_names()
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(f)
        self.words = word
        self.f = f.toarry()
        self.tfidf = tfidf
        return

    def calculate_web_similarity_by_text(self, web1: Website, web2: Website):
        index1 = self.url.index(web1.url)
        index2 = self.url.index(web2.url)
        word1 = self.words[index1]
        word2 = self.words[index2]
        tfidf1 = self.tfidf[index1]
        tfidf1 = self.tfidf[index2]
        # Calculate DocVec and return it.
        return 1

    def calculate_web_similarity_by_dom_tree(self, web1: Website, web2: Website):
        dom_tree1 = web1.get_dom_tree()
        dom_tree2 = web2.get_dom_tree()
        return 1

    def calculate_web_similarity(self, web1: Website, web2: Website):
        coeff1 = 1
        coeff2 = 0
        text_similarity = coeff1 * self.calculate_web_similarity_by_dom_tree(web1, web2)
        dom_tree_similarity = coeff2 * self.calculate_web_similarity_by_dom_tree(web1, web2)
        return text_similarity + dom_tree_similarity
