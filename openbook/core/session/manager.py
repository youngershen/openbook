# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen


class Manager(object):

    def __init__(self, backend = 'file'):
        self.backend = backend
        pass

    @classmethod
    def get_session(cls, session_id):
        pass

    @classmethod
    def create_session(cls):
        pass

    @classmethod
    def store_session(cls):
        pass


