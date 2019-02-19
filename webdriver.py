# -*- coding: utf-8 -*-

import requests
from lxml import etree
from selenium import webdriver


def download(src, name):
    dir = './pic/' + name + '.jpg'
    # print(dir)
    try:
        pic = requests.get(src, timeout=30)
        fp = open(dir, 'wb')
        fp.write(pic.content)
        fp.close()
    except Exception:
        print("error,%s 当前图片无法下载" % src)


driver = webdriver.Chrome('/Users/sgl/Downloads/chromedriver')

# print(type(driver))
for start in range(0, 15, 15):
    url = 'https://movie.douban.com/subject_search?search_text=' + \
        '周星驰' + '&cat=1002' + '&start=' + str(start)
    driver.get(url)
    # print(driver.page_source)
    # driver.page_source.setdefaultencoding('utf-8')
    html = etree.HTML(driver.page_source)
    src_xpath = "//*[@class='item-root']/a/img/@src"
    title_xpath = "//*[@class='item-root']/div[@class='detail']/div[@class='title']/a/text()"
    srcs = html.xpath(src_xpath)
    titles = html.xpath(title_xpath)
    # print(srcs,titles)
    for src, title in zip(srcs, titles):
        print(src)
        # print(title)
        title = title.replace(' ', '')
        print(title)
        download(src, title)
