# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen

import random


def generate_session_key_django(length=32, allow_chars='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'):
    key = ''.join(random.choice(allow_chars) for i in range(length))
    return key


