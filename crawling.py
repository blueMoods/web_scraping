# python2
# -*- coding: utf-8 -*

import re
import itertools
import urlparse
from download import download


# 网站地图爬虫
# 实测：很多网站没有 /sitemap.xml 页面。
def crawl_sitmap(url = "https://translate.google.com/sitemap.xml"):
    sitemap = download(url)
    links = re.findall("<loc>(.*?)</loc>", sitemap)
    for link in links:
        html = download(link)


# ID 遍历爬虫
# 实测：大部分网站没有 /view 目录。已发现有该目录的网站，id 是很长的 16 进制串
# 例如：http://dts-sync-data.cdn.bcebos.com/wenku/flow/360sitemap/360_sitemap_2412.xml
def crawl_id(url = "https://wenku.baidu.com"):
    max_errors = 5
    current_errors = 0
    for page in itertools.count(1):
        url_id = "%s/view/%d" %(url, page)
        html = download(url_id)
        if html is None:
            current_errors += 1
            if current_errors == max_errors:
                break
        else:
            current_errors = 0

# ID 链接爬虫
# 实测：
def crawl_link(seed_url = "http://home.ustc.edu.cn/~baohd/", link_regex = ".*2021.*", max_depth = 5):
    crawl_queue = [seed_url]

    # keep track which URL's have been seen before
    seen = {}
    seen[seed_url] = 0
    while crawl_queue:
        url = crawl_queue.pop()
        depth = seen[url]
        html = download(url)
        # print html
        if html != None and depth < max_depth:
            for link in get_links(html):
                if re.match(link_regex, link):
                    # form absolute link
                    link = urlparse.urljoin(seed_url, link)
                    # check if have already seen this url
                    if link not in seen:
                        seen[link] = depth + 1
                        crawl_queue.append(link)

def get_links(html):
    webpage_regex = re.compile("<a[^>]+href=['\"](.*?)['\"]", re.IGNORECASE)
    return webpage_regex.findall(html)
