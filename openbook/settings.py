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

#tornado settings
settings = dict()
settings['BASEDIR'] = BASEDIR
settings['TEMPLATEDIR'] = TEMPLATEDIR
settings['STATICDIR'] = STATICDIR
#debug
settings['DEBUG'] = DEBUG
#jinja2
settings['JINJA2'] = dict()
settings['JINJA2']['loader'] = FileSystemLoader(TEMPLATEDIR) 
settings['JINJA2']['auto_reload'] = DEBUG
settings['JINJA2']['autoescape'] = True
