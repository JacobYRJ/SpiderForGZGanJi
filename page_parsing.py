# -*- coding:utf-8 -*-
from bs4 import BeautifulSoup
import requests
import time
import pymongo
import random
import re

client = pymongo.MongoClient('localhost', 27017)
gzzhuan = client['gzzhuan']
url_list = gzzhuan['url_list']
item_info = gzzhuan['item_info']

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
    'http://60.191.47.54:81',
    'http://120.199.224.78:80',
    'http://211.143.155.172:80',
]
proxy_ip = random.choice(proxy_list)  # 随机获取代理ip
proxies = {'http': proxy_ip}


# spider 1
def get_links_from(channel, pages):
    # http://bj.ganji.com/ershoubijibendiannao/o3/
    # o for personal a for merchant
    list_view = '{}pn{}/'.format(channel, str(pages))
    print(list_view)
    print(channel.split('/')[3])
    wb_data = requests.get(list_view, headers=headers, proxies=proxies)
    time.sleep(2)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if soup.find('div', 'pager'):
        for link in soup.select('div.infocon > table.tbimg > tbody > tr.zzinfo td.t  a'):
            item_link = link.get('href').split('?')[0]
            if re.findall('(zhuanzhuan)', item_link):
                url_list.insert_one({'url': item_link, 'fenlei': channel.split('/')[3]})
                print(item_link)
            else:
                pass
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
# get_links_from('http://gz.58.com/diannao/', 1)
