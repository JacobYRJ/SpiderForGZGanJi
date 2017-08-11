# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import re

start_url = 'http://www.zhuanzhuan.com'
# url_host = 'http://gz.ganji.com'
gz = re.compile('(bj)', re.S)


def get_index_url(url):
    # url = start_url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # div.body_box2 > ul > li:nth-child(1)
    links = soup.select(' div.body_box2 > ul > li > a')
    for link in links:
        page_url = gz.sub('gz', str(link.get('href').split('?')[0]))
        print(page_url)

get_index_url(start_url)

channel_list = '''
    http://gz.58.com/diannao/
    http://gz.58.com/bijiben/
    http://gz.58.com/pbdn/
    http://gz.58.com/shouji/
    http://gz.58.com/shuma/
    http://gz.58.com/jiadian/
    http://gz.58.com/ershoujiaju/
    http://gz.58.com/jujia/
    http://gz.58.com/fushi/
    http://gz.58.com/meirong/
    http://gz.58.com/wenti/
    http://gz.58.com/tushu/
    http://gz.58.com/danche/
    http://gz.58.com/diandongche/
    http://gz.58.com/zixingche/
    http://gz.58.com/yingyou/
'''

# get_index_url(start_url)
