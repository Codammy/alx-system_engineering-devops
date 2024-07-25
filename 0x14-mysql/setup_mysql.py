#!/usr/bin/python3
"""installs mysql on remote servers"""
from fabric.api import sudo, prefix, run


def install_db():
    """installs mysql"""
    with prefix("apt update"):
        if sudo("apt install -y mysql-server").succeeded:
            print("OK.")


def create_db_user(user, passwd):
    """create database user"""
    host = "localhost"
    script = '"CREATE USER IF NOT EXISTS {}@{} IDENTIFIED BY \'{}\';"'.format(
             user, host, passwd
             )
    grant = '"GRANT REPLICATION CLIENT ON *.* TO holberton_user@localhost;"'
    sudo("echo {} {} | mysql".format(script, grant))
