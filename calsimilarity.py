# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webparser.py
@Time    :2020/3/24 14:08
"""

import webparser


def calculate_web_similarity(web1:webparser.WebParser, web2:webparser.WebParser):
    coeff1 = 0.5
    coeff2 = 0.5
    text_similarity = coeff1 * calculate_web_similarity_by_text(web1, web2)
    dom_tree_similarity = coeff2 * calculate_web_similarity_by_dom_tree(web1, web2)
    return text_similarity + dom_tree_similarity


def calculate_web_similarity_by_text(web1, web2):
    text1 = web1.get_text()
    text2 = web2.get_text()
    return 1


def calculate_web_similarity_by_dom_tree(web1, web2):
    dom_tree1 = web1.get_dom_tree()
    dom_tree2 = web2.get_dom_tree()
    return 1