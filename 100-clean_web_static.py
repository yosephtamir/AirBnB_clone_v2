#!/usr/bin/python3
"""This script is used to deploy a static web to the ff servers"""
from fabric.api import run, env, put, local, runs_once, lcd, cd
from datetime import datetime
from time import strftime
from os import path
env.hosts = ["18.210.20.171", "52.23.244.251"]


@runs_once
def do_pack():
    '''a Fabric method that generates a .tgz '''
    local("mkdir -p versions")
    date = datetime.utcnow()
    path = ("versions/web_static_{}.tgz".format
            (datetime.strftime(date, "%Y%m%d%H%M%S")))
    local("tar -cvzf {} web_static".format(path))
    return path


def do_deploy(archive_path):
    """a fabric/python method to deploy a webstatic"""
    if path.exists(archive_path):
        splitPath = archive_path.split("/")[1]
        splitExt = splitPath.split('.')[0]
        extractTo = "/data/web_static/releases/{}".format(splitExt)
        put(archive_path, "/tmp/")
        run("mkdir -p {}".format(extractTo))
        run("tar -xzf /tmp/{} -C {}".format(splitPath, extractTo))
        run("rm /tmp/{}".format(splitPath))
        run("mv {}/web_static/* {}".format(extractTo, extractTo))
        run("rm -rf {}/web_static".format(extractTo))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(extractTo))
        return True
    else:
        return False


def deploy():
    """Used to deploy to webserver"""
    archive_path = do_pack()
    if archive_path:
        return do_deploy(archive_path)
    else:
        return None


def do_clean(number=0):
    """Used to delete unnesessary files"""

    number = int(number)
    if number == 0:
        number = 1
    # delete from local
    with lcd("versions"):
        lists = local("ls -rd web_static_*", capture=True).split()
        lists = lists[number:]
        for file in lists:
            local("rm -rf {}".format(file))

    # delete from the webserver
    with cd("/data/web_static/releases"):
        lists = run("ls -rd web_static_*").split()
        lists = lists[number:]
        for folder in lists:
            run("rm -rf {}".format(folder))
