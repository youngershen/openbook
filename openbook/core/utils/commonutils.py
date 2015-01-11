# -*- coding: utf-8 -*-
# author  : younger shen
# email   : younger.x.shen@gmail.com
# project : Playwork
# date    : 15/1/11 下午9:22

import time
import hashlib
from openbook.settings import settings

def make_urls_util(prefix, urls):
    correct_urls = []
    for url in urls:
        url_tuple = (prefix + url[0], url[1])
        correct_urls.append(url_tuple)

    return correct_urls

def make_timestamp():
    return time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))

def gen_password(password):
    md5 = hashlib.md5(password + settings['SALT']).hexdigest()

