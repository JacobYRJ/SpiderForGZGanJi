# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
import re

client = pymongo.MongoClient('localhost', 27017)
gzganji = client['gzganji']
url_list = gzganji['url_list']
item_info = gzganji['item_info']

replace_label = re.compile(r'<[^>]+>', re.S)

headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/47.0.2526.111 Safari/537.36',
    'Connection': 'keep-alive'
}

# http://cn-proxy.com/
proxy_list = [
    # 'http://117.177.250.151:8081',
    # 'http://111.85.219.250:3129',
    # 'http://122.70.183.138:8118',
    'http://122.192.74.83:8080',
    'http://219.153.76.77:8080',
    'http://61.130.97.212:8099',
]
proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
proxies = {'http': proxy_ip}


# spider 1
def get_links_from(channel, pages, who_sells='o'):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    list_view = '{}{}{}/'.format(channel, str(who_sells), str(pages))
    print(list_view)
    wb_data = requests.get(list_view, headers=headers, proxies=proxies)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # print(soup.select('td > a.t'))
    # jingzhun > tbody > tr:nth-child(2) > td.t > a
    if soup.find('ul', 'pageLink'):
        for link in soup.select('td.t > a'):
            # print(2)
            item_link = link.get('href').split('?')[0]
            url_list.insert_one({'url': item_link})
            print(item_link)
            # return urls
    else:
        # It's the last page !
        print('pass')
        pass

# spider 2


def get_item_info_from(url, data=None):
    wb_data = requests.get(url, headers=headers, proxies=proxies)
    if wb_data.status_code == 404:
        print('pass')
        pass
    else:
        try:
            soup = BeautifulSoup(wb_data.text, 'lxml')
            print(1)
            data = {
                'title': soup.find('h1', 'info_titile').text,
                'price': replace_label.sub('', str(soup.select('div.price_li > span > i')[0])),
                'area': replace_label.sub('', str(soup.select('div.palce_li > span > i')[0])),
                'want_person': re.findall('\d+', soup.find('span', 'want_person').text)[0],
                'look_time': re.findall('\d+', soup.find('span', 'look_time').text)[0],
                'url': url,
            }
            # data = {
            #     'title':soup.title.text.strip(),
            #     'price':soup.select('.f22.fc-orange.f-type')[0].text.strip(),
            #     'pub_date':soup.select('.pr-5')[0].text.strip().split(' ')[0],
            #      'area':list(map(lambda x:x.text,soup.select('ul.det-infor > li:nth-of-type(3) > a'))),
            #     'cates':list(soup.select('ul.det-infor > li:nth-of-type(1) > span')[0].stripped_strings),
            #     'url':url,
            # }

            item_info.insert_one(data)
            print(data)

        except AttributeError:
            print('AttributeError')
            pass
        except IndexError:
            print('IndexError')
            pass

# get_item_info_from('http://zhuanzhuan.ganji.com/detail/804851128506679302z.shtml')
# get_links_from('http://gz.ganji.com/shouji/', 1)
