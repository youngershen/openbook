# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen
import os
import pickle
import cjson
from errors import SessionSettingsError
from utils import generate_session_key_django


class BaseBackend(object):

    def __init__(self):
        pass


class MySQLSessionBackendMixin(BaseBackend):
    pass


class RedisSessionBackendMixin(BaseBackend):
    pass


class MemcachedSessionBackendMixin(BaseBackend):
    pass


class FileSessionBackendMixin(BaseBackend):
    # create
    # save
    # load
    # delete
    def session_exists(self, session_id):
        return os.path.exists(self.settings.get('PATH') + session_id + '.session')

    def create(self):
        file_path = self.settings.get('PATH', None)
        if not file_path:
            raise SessionSettingsError("'PATH' is not in your session settings")
            exit()

        session_id = generate_session_key_django()
        while True:
            if not self.session_exists(session_id):
                break
            else:
                session_id = generate_session_key_django()

        setattr(self, 'session_path', self.settings.get('PATH') + session_id + '.session')
        setattr(self, 'session_id', session_id)
        self.save()

    def save(self):
        with open(self.session_path, 'w') as f:
            pickle.dump(self, f, protocol=self.settings.get('COMPRESSED', 0))
            # f.write(self.to_json())

    @classmethod
    def load(cls, session_id):
        pass

    def to_json(self):
        json_dict = dict()
        json_dict['session_id'] = self.session_id
        json_dict['expire'] = self.expire
        json_dict['expire_time'] = self.expire_time
        json_dict['create_time'] = self.create_time
        json_dict['settings']    = self.settings
        json_dict['cache']       = self.cache
        return cjson.encode(json_dict)