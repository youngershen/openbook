#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

import os
import sys
from jinja2 import Environment
from jinja2 import PackageLoader
from jinja2 import FileSystemLoader

sys.path[0:0] = ["../"]
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
