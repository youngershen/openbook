#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#support session for tornado web framework 
import pickle
import time
import hashlib
import os

class YSessionManager(object):
    settings = None
    sessions = dict()

    def __init__(self, settings):
        self.settings = settings
    def generateSessionID(self):
        return hashlib.md5( str(time.time()) + self.settings.get('SECRET_KEY')).hexdigest()        

    def serialize(self, session_id):
        session = self.sessions[session_id]
        if session is not None:
            with open(self.settings['DIR'] + '/' + session_id + '.session', 'w') as file:
                pickle.dump(session, file)


    def session_add(self, session_id, key, value):
        session = self.get_session(session_id=session_id)
        session.add(key, value)
        self.serialize(session_id)

    def session_get(self, session_id, key):
        session = self.get_session(session_id=session_id)
        if session is None:
            return None
        return session.get(key)

    def session_pop(self, session_id, key):
        session = self.get_session(session_id=session_id)
        if session is None:
            return None
        return session.pop(key)

    def get_session(self, session_id=None):

        if session_id is None:
            session_id = self.generateSessionID()
            
            self.sessions[session_id] = YSession(session_id=session_id)
            self.serialize(session_id)
            return session_id
        
        if self.sessions.get(session_id) is not None:
            return self.sessions.get(session_id)
        
        elif self.warm_up(session_id) is not None:
            return self.warm_up(session_id)

    def warm_up(self, session_id):
        try:
            with open(self.settings['DIR'] + '/' + session_id + '.session' ,'r') as file:
                data = pickle.load(file)
        except IOError as e:
            print e
            return None
        else:
            self.sessions[session_id] = data
            return self.sessions.get(session_id)
        #warp up from local file
    
    def clean_up(self):
        pass
        #clean the over due session files
        

class YSession(object):
    
    def __init__(self, session_id=None, **kwargs):
        self.data = dict()
        self.session_id = session_id
        self.data.update(**kwargs)        

    def add(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data.get(key)

    def pop(self, key):
        return self.data.pop(key)
    
    def __unicode__(self):
        return str(self.data.keys())

    def __str__(self):
        return self.__unicode__()

def main():
    manager = YSessionManager()
    #s1 = manager.get_session('s1')
    #manager.session_add('s1', 'hat', 'hat')
    #manager.session_add('s1', 'name', 'younger')
    #print manager.session_get('s1', 'name')
    #print manager.generateSessionID()

    #session_id = manager.get_session()
    #manager.session_add(session_id, 'name', 'younger')
    print manager.session_get('3937f12481784284c2608dafa33efd96s', 'name')
if __name__ == '__main__':
    main()
