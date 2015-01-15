# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen
import os
import pickle
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
    # sfsdf23sfssff.session
    def exists(self, key):
        return os.path.exists(self.session_path)

    def create(self):
        file_path = self.settings.get('PATH', None)
        if not file_path:
            raise SessionSettingsError("'PATH' is not in your session settings")
            exit()

        key = generate_session_key_django()
        while True:
            if not self.exists(key):
                break
            else:
                key = generate_session_key_django()

        self.session_path = self.settings.get('PATH') + key + '.session'
        self.save()

    def save(self):
        with open(self.session_path, 'w') as f:
            pickle.dump(self, protocol=self.settings.get('COMPRESSED', 0), f)