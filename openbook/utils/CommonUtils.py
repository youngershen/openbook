#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

def make_urls_util(prefix, urls):
    correct_urls = []
    for url in urls:
        url_tuple = (prefix + url[0], url[1])
        correct_urls.append(url_tuple)

    return correct_urls
