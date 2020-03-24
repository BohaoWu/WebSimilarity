# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :webparser.py
@Time    :2020/3/24 14:08
"""

import calrelevance
import calsimilarity
import webcrawler


if __name__ == "__main__":
    seed_web = "url"
    crawler = webcrawler.Crawler()
    crawler.add_website(seed_web)
    while(len(crawler.websites) > 0):
        crawler.crawler()

        # According to relevance， decide website which we have to crawl next generation
        thed1 = 0.5
        for i in crawler.websites:
            if calrelevance.calculate_relevance(i) < thed1:
                crawler.websites.remove(i)

        thed2 = 0.5
        # According to similarity, decide websites which may have same topic with seed website
        for i in  crawler.websites:
            if calsimilarity.calculate_web_similarity(i, seed_web) < thed2:
                crawler.websites.remove(i)

    print("Web crawler finshed.")


