# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests


start_url = 'http://gz.ganji.com/wu/'
url_host = 'http://gz.ganji.com'

def get_index_url(url):
    # url = start_url
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    links = soup.select('.fenlei > dt > a')
    for link in links:
        page_url = url_host + link.get('href')
        print(page_url)

get_index_url(start_url)

channel_list = '''
    http://gz.ganji.com/jiaju/
    http://gz.ganji.com/rirongbaihuo/
    http://gz.ganji.com/shouji/
    http://gz.ganji.com/bangong/
    http://gz.ganji.com/nongyongpin/
    http://gz.ganji.com/jiadian/
    http://gz.ganji.com/ershoubijibendiannao/
    http://gz.ganji.com/ruanjiantushu/
    http://gz.ganji.com/yingyouyunfu/
    http://gz.ganji.com/diannao/
    http://gz.ganji.com/xianzhilipin/
    http://gz.ganji.com/fushixiaobaxuemao/
    http://gz.ganji.com/meironghuazhuang/
    http://gz.ganji.com/shuma/
    http://gz.ganji.com/laonianyongpin/
'''

# get_index_url(start_url)
