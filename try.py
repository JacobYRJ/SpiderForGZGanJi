# -*- coding:utf-8 -*-
from page_parsing import get_item_info_from, url_list, item_info, get_links_from
from page_parsing import url_list


# from channel_extracing import channel_list
# for i in channel_list.split():
#     fenlei = i.split('/')[3]
#     print(fenlei)

db_urls = [item['url'] for item in url_list.find()]
index_urls = [item['url'] for item in item_info.find()]
x = set(db_urls)
y = set(index_urls)
rest_of_urls = x - y
print(len(rest_of_urls))
# for i in rest_of_urls:
#     print(i)


# url_t = url_list.find().limit(10)
# def test(url_li):
#     for i in url_li:
#         print(i['url'])

# test(url_t)
# def try_to_make(a_mess):
#     try:
#         print(1/a_mess)
#     except (ZeroDivisionError,TypeError):
#         print('ok~')


# try_to_make('0')
