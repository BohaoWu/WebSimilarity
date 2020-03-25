# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :main.py
@Time    :2020/3/24 14:08
"""

import calrelevance
import calsimilarity
import webclassifier
import webcrawler
import website


if __name__ == "__main__":
    seed_web = ['url']
    crawlers = []
    classifier = webclassifier.Classifier()

    # Each seed website is used as root of crawler.
    for url in seed_web:
        crawler = webcrawler.Crawler()
        crawler.set_root_website(website.Website(url, webcrawler.get_soup(url), './web_source' + url, True, 1))
        crawlers.append(crawler)

    # Do the crawler!
    count = len(crawlers)
    while count > 0:
        count = 0
        for crawler in crawlers:
            crawler.crawler()
            count = count + len(crawler.website_nodes)
    print("Web crawler finshed.")

    # Save similar doc



