# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen
import cjson
import pickle
from openbook.settings.settings import *


class FileSessionAgent(object):

    def __init__(self, settings=None):
        self.settings = settings

    def load(self, session_id):
        session_entity = self.get_session_content(session_id)
        return session_entity

    def get_session_content(self, session_id):
        file_path = self.settings.get('PATH') + session_id + '.session'

        try:
            with open(file_path, 'r') as f:
                return pickle.load(f)
        except IOError as e:
            return None


class Manager(object):

    def __init__(self, settings=None):
        self.setting = settings

    @classmethod
    def get_session(cls, session_id):
        pass

    @classmethod
    def create_session(cls):
        pass

    @classmethod
    def store_session(cls):
        pass


if __name__ == '__main__':
    agent = FileSessionAgent(settings=settings['SESSION'])
    session = agent.load('PJK4XO6qyxyAr81kVW08fvJ3kMeP0ZzG')
    print session.get_session_id()