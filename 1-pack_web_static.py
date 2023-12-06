#!/usr/bin/python3
'''A Fabric script to generate .tgz archive'''

from fabric.api import local
from datetime import datetime
from time import strftime


def do_pack():
   '''generates archive a .tgz archie'''

    local("mkdir -p versions")
    path = ("versions/web_static_{}.tgz".format(datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")))
    output = local("tar -cvzf {} web_static".format(path))
    if output.failed:
        return None
        return path
