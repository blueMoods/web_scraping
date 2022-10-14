# python2
# -*- coding: utf-8 -*

import re
from download import download
from bs4 import BeautifulSoup
import lxml.html


# 抓取：正则表达式
# 默认参数为：抓取博主名下所有的博客名称
def scrap_regular(url = "http://home.ustc.edu.cn/~baohd/", regular = 'class="post-title-link" itemprop="url">(.*?)</a>'):
    html = download(url)
    if html:
        blobs = re.findall(regular, html)
        print "Scraping with Regular Expression, results are as blew:\n"
        for blob in blobs:
            print unicode(blob, encoding="utf-8")
        print "\n"

# 抓取：Beautiful Soup
# 安装：pip install beautifulsoup4
# 默认参数为：抓取博主名下所有的博客名称
def scrap_beautifulsoup(url = "http://home.ustc.edu.cn/~baohd/", key = "class", value = "post-title-link"):
    html = download(url)
    if html:
        soup = BeautifulSoup(html, "html.parser")
        # fixed_html = soup.prettify()
        blobs = soup.find_all(attrs={key:value})
        print "Scraping with Beautiful Soup, results are as blew:\n"
        for blob in blobs:
            print blob.text
        print "\n"

# 抓取：Lxml
# 安装：pip install lxml
#      pip install cssselect
# 默认参数为：抓取博主名下所有的博客名称
def scrap_lxml(url = "http://home.ustc.edu.cn/~baohd/", select = "a.post-title-link"):
    html = download(url)
    if html:
        tree = lxml.html.fromstring(html)
        # fixed_html = lxml.html.tostring(tree, pretty_print=True)
        blobs = tree.cssselect(select)
        # blobs = tree.cssselect("a.post-title-link")
        # blobs = tree.cssselect("header.post-header a.post-title-link")
        # blobs = tree.cssselect("header.post-header > h2.post-title > a.post-title-link")
        print "Scraping with Lxml, results are as blew:\n"
        for blob in blobs:
            print blob.text_content()
        print "\n"

if __name__ == '__main__':
    # scrap_regular()
    # scrap_beautifulsoup()
    scrap_lxml()