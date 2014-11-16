#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

#support session for tornado web framework 
import pickle
#from openbook.settings import settings
settings=dict()
settings['SESSION'] = dict()
settings['SESSION']['DIR'] = './'

class Utils(object):
    @staticmethod
    def generateSessionId():
        pass
        

class YSessionManager(object):
    settings = settings['SESSION']
    sessions = dict()

    def __init__(self):
        #worm up
        pass

    def serialize(self, session_id):
        session = self.sessions[session_id]
        if session is not None:

            with open(self.settings['DIR'] + '/' + session_id + '.session', 'w') as file:
                pickle.dump(session, file)



    def session_add(self, session_id, key, value):
        session = self.get_session(session_id)
        session.add(key, value)
        self.serialize(session_id)

    def session_get(self, session_id, key):
        session = self.get_session(session_id)
        return session.get(key)

    def session_pop(self, session_id, key):
        session = self.get_session(session_id)
        return session.pop(key)

    def get_session(self, session_id):
        
        if self.sessions.get(session_id) is not None:
            return self.sessions.get(session_id)
        
        elif self.warm_up(session_id) is not None:
            return self.warm_up(session_id)
        else:
            
            self.sessions[session_id] = YSession(session_id = session_id)
            self.serialize(session_id)
            return self.sessions.get(session_id)

    def warm_up(self, session_id):
        try:
            with open(self.settings['DIR'] + '/' + session_id + '.session' ,'r') as file:
                data = pickle.load(file)
        except IOError as e:
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
    manager.session_add('s1', 'name', 'younger')
    print manager.session_get('s1', 'name')
    

if __name__ == '__main__':
    main()
