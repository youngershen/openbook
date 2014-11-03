#!/usr/bin/env python
from migrate.versioning.shell import main

if __name__ == '__main__':
    main(url='mysql://root:root@127.0.0.1:3306/openbook_dev', debug='False', six="<module 'six' from '/home/youngershen/dev/projects/openbook/env/local/lib/python2.7/site-packages/six.pyc'>", repository='migration')
