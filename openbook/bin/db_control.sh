#/usr/bin/bash
python migration/manage.py version_control mysql://root:root@127.0.0.1:3306/openbook_dev migration
