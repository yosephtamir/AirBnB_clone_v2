#!/usr/bin/python3
'''a Fabric script that generates a .tgz archive
from the contents of the web_static folder'''

from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
    '''a Fabric method that generates a .tgz '''
    local("mkdir -p versions")
    date = datetime.utcnow()
    path = ("versions/web_static_{}.tgz".format
            (datetime.strftime(date, "%Y%m%d%H%M%S")))
    if local("tar -cvzf {} web_static".format(path)).failed:
        return None
    return path
