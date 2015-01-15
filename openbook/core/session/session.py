# -*- coding:utf-8 -*-
# PROJECT_NAME : openbook
# FILE_NAME    : 
# AUTHOR       : younger shen
import time
from openbook.core.session.errors import UnSafeSessionSettingError
from openbook.settings import settings

settings = settings['SESSION']


class SessionBase(object):

    def __init__(self, key=None, cache=None, expire=None):

        self.key = key
        self.create_time = time.time()

        if expire:
            self.expire = expire
        else:
            self.expire = settings['EXPIRE']

        if cache:
            self.cache = cache
        else:
            self.cache = dict()

    def get_expire_time(self):
        return self.expire

    def set_expore_time(self, time):
        self.expire

    def set(self, key, value):

        self.cache.update({key: value})

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

    def get_expire(self):
        return self.expire

    def set_expires(self, expire):
        self.expire = expire

    def create(self):
        raise NotImplementedError('subclasses of SessionBase must provide a create() method')

    def save(self):
        raise NotImplementedError('subclasses of SessionBase must provide a save() method')

    def load(self):
        raise NotImplementedError('subclasses of SessionBase must provide a load() method')
    
    def delete(self):
        raise NotImplementedError('subclasses of SessionBase must provide a delete() method')


class SessionFile(SessionBase):
    pass


def main():
    pass

if __name__ == '__main__':
    main
