#!/usr/bin/env python
#-*- coding: utf-8 -*-
# author : younger shen
# email  : younger.x.shen@gmail.com

# scraffold script for openbook project

import sys
import os
import getopt
import shutil

CWD = os.getcwd()
APPDIR = os.getcwd() + "/scaffold/app"

def usage():
    print "-h for help \r"
    print "-a appname for create a app in appname folder\r"

def version():
    print "scraffold for openbook v0.0.1"


def parse_file(appname):
    
    content = ""
    with open("./" + appname + "/views/IndexView.py", "r") as f:
        content = f.read().replace("MODULE_NAME", "'" + appname + "'")
    
    with open("./" + appname + "/views/IndexView.py", 'w') as f:
        f.write(content)
        f.flush()

def create_app(appname):
    print "create app " + appname + "\r"
    if os.path.exists(CWD + "/" + appname):
        print "app dir already exists"
        sys.exit()
    else:
        shutil.copytree(APPDIR, "./" + appname)
        parse_file(appname)
    

try:
    opts, args = getopt.getopt(sys.argv[1:], "vha:")
except:
    usage()
    sys.exit()
if len(opts) == 0:
    usage()
    sys.exit()

for op, value in opts:
    if op == '-a':
        #create app
        create_app(value)
        sys.exit()
    if op == '-v':
        version()
    elif op == '-h':
        usage()
        sys.exit()
    else:
        usage()
        sys.exit()
