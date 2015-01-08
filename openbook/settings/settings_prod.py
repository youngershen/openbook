#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import os
import sys

sys.path[0:0] = ["../"]

from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import FileSystemLoader
from openbook.vendor.session.YSession import YSessionManager

BASEDIR = os.getcwd()
TEMPLATEDIR = BASEDIR + "/templates/"
STATICDIR = BASEDIR + "/static/"


DEBUG = True

#settings
settings = dict()
settings['BASEDIR'] = BASEDIR
settings['TEMPLATEDIR'] = TEMPLATEDIR
settings['STATICDIR'] = STATICDIR
settings['SALT']      = "are you thinking what i am thinking"
settings['DATABASE']  = 'mysql'
settings['DBUSER']    = 'root'
settings['DBPASS']    = 'root'
settings['DBNAME']    = 'openbook_dev'
settings['DBPREFIX']  = 'ob_'
settings['DBHOST']    = '127.0.0.1'
settings['DBPORT']    = '3306'
#tornado
settings['tornado'] = dict()
settings['tornado']['debug'] = DEBUG
settings['tornado']['autoreload'] = DEBUG
settings['tornado']['login_url'] = '/account/login'
settings['tornado']['xsrf_cookies'] = True
settings['tornado']['cookie_secret'] = "are you thinking what i am thinking"
settings['tornado']['static_path'] = STATICDIR
#debug
settings['DEBUG'] = DEBUG
#jinja2
settings['JINJA2'] = dict()
settings['JINJA2']['loader'] = FileSystemLoader(TEMPLATEDIR) 
settings['JINJA2']['auto_reload'] = DEBUG
settings['JINJA2']['autoescape'] = True
#db config
settings['DBCONFIG'] = dict()
settings['DBCONFIG']['encoding'] = 'utf8'
settings['DBCONFIG']['echo'] = DEBUG

#session config
settings['SESSION'] = dict()
settings['SESSION']['BACKEND'] = 'mysql|redis|memcached|file' #not used yet 
settings['SESSION']['DIR'] = BASEDIR + '/tmp/sessions' #directory to store the session file
settings['SESSION']['SECRET_KEY'] = 'are you thinking what i am thinking'
settings['SESSION']['EXPIRE'] = 24 * 60 * 7
settings['SESSION']['MANAGER'] = YSessionManager
