#!/usr/bin/python3
"""This script is used to deploy a static web to the ff servers"""
from fabric.api import run, env, put
from datetime import datetime
from os import path
env.hosts = ["18.210.20.171", "52.23.244.251"]


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
