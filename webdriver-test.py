# -*- coding: utf-8 -*-

import requests
from lxml import etree
from selenium import webdriver


driver = webdriver.Chrome('/Users/sgl/Downloads/chromedriver')

# print(type(driver))
for start in range(0, 15, 15):
    url = 'https://movie.douban.com/subject_search?search_text=' + \
        '周星驰' + '&cat=1002' + '&start=' + str(start)
    driver.get(url)
    # print(driver.page_source)
    # driver.page_source.setdefaultencoding('utf-8')
    html = etree.HTML(driver.page_source)
    title_xpath = "//*[@class='item-root']/div[@class='detail']/div[@class='title']/a/text()"
    score_xpath = "//*[@class='item-root']/div[@class='detail']//span[@class='pl']/text()"

    titles = html.xpath(title_xpath)
    scores = html.xpath(score_xpath)

    # print(srcs,titles)
    for title, score in zip(titles, scores):
        title = title.replace(' ', '')
        print(title + ' ' + score)
