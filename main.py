# -*- coding:utf-8 -*-
from multiprocessing import Pool
from page_parsing import get_item_info_from, url_list, item_info, get_links_from
# from channel_extracing import channel_list
import signal
import sys

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y


def get_all_links_from(channel):
    for i in range(26, 60):
        get_links_from(channel, i)


def get_all_items_from(url_li):
    get_item_info_from(url_li)
    # print(url_li)


def quit(signum, frame):
    print('You choose to stop me')
    sys.exit()

if __name__ == '__main__':
    signal.signal(signal.SIGINT, quit)
    signal.signal(signal.SIGTERM, quit)
    pool = Pool(processes=4)
    # # pool = Pool()
    # pool.map(get_all_links_from, channel_list.split())
    pool.map(get_all_items_from, [rest_url for rest_url in rest_of_urls])
    pool.close()
    pool.join()
