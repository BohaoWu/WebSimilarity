# -*- coding: utf-8 -*-

"""
@Author  :AkiyamaN
@File    :main.py
@Time    :2020/3/24 14:08
"""

import webclassifier
import webcrawler
import website


if __name__ == "__main__":
    seed_web_url = ['https://bohaowu.github.io/BohaoWu/index_en.html']
    seed_web = []
    crawlers = []

    # Crawl seed website.
    for url in seed_web_url:
        web = website.Website(url, webcrawler.get_soup(url), './web_source/' + url, True, 1)
        seed_web.append(web)
    print('Seed websites have been crawled.')

    # Add seed into classifier
    classifier = webclassifier.Classifier(seed_web)

    # Each seed website is used as root of crawler.
    for seed in seed_web:
        crawler = webcrawler.Crawler()
        crawler.set_root_website(seed)
        crawlers.append(crawler)
    print('Crawlers have been built.')

    # Do the crawler!
    round_count = 1
    count = len(crawlers)
    while count > 0:
        count = 0
        for crawler in crawlers:
            crawler.crawler(classifier)
            count = count + len(crawler.website_nodes)
        round_count += 1
        print('This the %s round of crawler.' % (round_count))
    print("Web crawler finshed.")

    with open('corpus.txt', 'a') as f:
        for i in classifier.corpus:
            f.write(i)
    print("Corpus has been saved.")

    # Save similar doc



