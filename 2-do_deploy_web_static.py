#!/usr/bin/python3
"""
a Fabric script (based on the file 1-pack_web_static.py) that distributes an
archive to your web servers, using the function do_deploy:
"""
from fabric.api import put, run, env
from os import path


env.use_ssh_config = True
env.hosts = ["web-01", "web-02"]


def do_deploy(archive_path):
    """
    a method to deploy to webserver
    """
    if path.exists(archive_path):
        thetar = archive_path.split("/")[-1]
        serverFolder = "/data/web_static/releases/{}".format(thetar[:-4])
        run("mkdir -p {}".format(serverFolder))
        put(archive_path, "/tmp/")
        run("tar -xzf /tmp/{} -C {}".format(thetar, serverFolder))
        run("rm /tmp/{}".format(thetar))
        run("mv -f {}/web_static/* {}/".format(serverFolder, serverFolder))
        run('rm -rf {}/web_static'.format(serverFolder))
        run("rm -rf /data/web_static/current")
        run("ln -s {} /data/web_static/current".format(serverFolder))
        return True
    else:
        return False
