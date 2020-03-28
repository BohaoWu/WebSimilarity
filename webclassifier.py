# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webclassifier.py
@Time    :2020/3/24 21:08
"""

from gensim.scripts.glove2word2vec import glove2word2vec
from gensim.models import KeyedVectors
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer

from website import Website


class Classifier:
    """
    This class stores text of website. Calculate tf-idf for crawler.
    """

    def __init__(self, seed_websites, threshold=0.5):
        self.url = []
        for seed in seed_websites:
            self.url.append(seed.url)
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

        # Load glove
        word2vec_output_file = 'glove.6B.50d.word2vec.txt'
        glove_input_file = 'glove.6B.50d.txt'
        (self.count, self.dimension) = glove2word2vec(glove_input_file, word2vec_output_file)
        print("Glove model has been loaded, count is %s, dimension is %s." % (self.count, self.dimension))
        # Load model
        self.glove_model = KeyedVectors.load_word2vec_format(word2vec_output_file, binary=False)
        print(self.glove_model['snow'])
        print(self.glove_model.most_similar('snow'))
        return

    def set_seed_website(self, seed_websites):
        self.seed_websites = seed_websites
        return

    def add_website(self, website:Website):
        print(website.url, 'has been added into classifier.')
        self.url.append(website.url)
        self.websites.append(website)
        self.corpus.append(website.get_text())
        return

    def cal(self):
        # Refresh tf-idf
        vectorizer = CountVectorizer()
        f = vectorizer.fit_transform(self.corpus)
        word = vectorizer.get_feature_names()
        transformer = TfidfTransformer()
        tfidf = transformer.fit_transform(f)
        self.words = word
        self.f = f.toarray()
        self.tfidf = tfidf.toarray()
        return

    def calculate_web_similarity_by_text(self, web1: Website, web2: Website):
        index1 = self.url.index(web1.url)
        index2 = self.url.index(web2.url)
        tfidf1 = self.tfidf[index1].data
        tfidf2 = self.tfidf[index2].data

        # Calculate DocVec and return it.
        doc_vec1 = np.array([0 for i in range(self.dimension)])
        doc_vec2 = np.array([0 for i in range(self.dimension)])
        for i in range(len(self.words)):
            if self.words[i] in self.glove_model.index2word:
                doc_vec1 = doc_vec1 + tfidf1[i] * self.glove_model[self.words[i]]
                doc_vec2 = doc_vec2 + tfidf2[i] * self.glove_model[self.words[i]]
        return self.euclidean_distance(doc_vec1, doc_vec2)

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

    def cosine(self, x, y):
        sum_xy = 0.0
        norm_x = 0.0
        norm_y = 0.0
        for a, b in zip(x, y):
            sum_xy = sum_xy + a * b
            norm_x = norm_x + a ** 2
            norm_y = norm_y + b ** 2
        if norm_x == 0.0 or norm_y == 0.0:
            return -1
        else:
            return sum_xy/((norm_x * norm_y) ** 0.5)

    def euclidean_distance(self, x, y):
        d = 0
        for a, b in zip(x, y):
            d += (a-b) ** 2
        return d**0.5


if __name__ == '__main__':
    classifier = Classifier([])
