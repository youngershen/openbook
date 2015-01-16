# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen
import time
from abc import ABCMeta
from errors import UnSafeSessionSettingError
from errors import SessionSettingsError
from backends import FileSessionBackendMixin


class SessionBase(object):
    __metaclass__ = ABCMeta

    def __init__(self, cache=None, expire=None, settings=None):

        self.create_time = time.time()
        self.settings = settings
        if expire:
            self.expire = expire
        else:
            if 'EXPIRE' not in settings:
                raise SessionSettingsError("'EXPIRE' is not in your session settings")
            else:
                self.expire = settings['EXPIRE']

        self.expire_time = self.create_time + self.expire

        if cache:
            self.cache = cache
        else:
            self.cache = dict()

        self.create()

    def get_expire_time(self):
        return self.expire_time

    def get_expire(self):
        return self.expire

    def set_expire_time(self, ex_time):
        self.expire = ex_time
        self.expire_time = self.create_time + self.expire

    def get_create_time(self):
        return self.create_time

    def set(self, key, value):

        self.cache.update({key: value})
        self.save()

    def safe_set(self, key, value, force=False):

        if key not in self.cache:
            self.cache.update({key: value})
        else:
            if force:
                self.cache.update({key: value})
            else:
                raise UnSafeSessionSettingError('unsafe setting action unless you set the force flag to TRUE')

    def get(self, key):
        return self.cache.get(key, None)

    def pop(self, key):
        return self.cache.pop(key)

    def popitem(self):
        return self.cache.popitem()

    def update(self, _dict):
        self.cache.update(_dict)

    def keys(self):
        return self.cache.keys()

    def items(self):
        return self.cache.items()

    def has_key(self, key):
        return key in self.cache

    def exists(self, key):
        return key in self.cache

    def iterkeys(self):
        return self.cache.iterkeys()

    def itervalues(self):
        return self.itervalues()

    def __contains__(self, item):
        return item in self.cache

    def __iter__(self):
        return self.cache.__iter__()

    def clear(self):
        self.cache.clear()

    def iteritems(self):
        return self.iteritems()

    def is_empty(self):
        return len(self.cache.key()) == 0

    # def create(self):
    #     raise NotImplementedError('subclasses of SessionBase must provide a create() method')

    # def save(self):
    #     raise NotImplementedError('subclasses of SessionBase must provide a save() method')

    # def load(self):
    #     raise NotImplementedError('subclasses of SessionBase must provide a load() method')
    
    # def delete(self):
    #     raise NotImplementedError('subclasses of SessionBase must provide a delete() method')


class FileSession(SessionBase, FileSessionBackendMixin):
    pass
