#!/usr/bin/env python
# -*- coding:utf-8 -*-

__Author__ = "HackFun"
__Date__ = "2018/6/1 下午12:25"

from fabric.api import *

env.hosts = ['47.95.237.36']
env.user = 'root'
env.password = '123456'


def hello():
    print 'hello world'


def deploy():
    with cd('/root/workspaces/ProgramFiles/Py2Code/HFOnline'):
        run('git pull')
        sudo('supervisorctl restart hfapp')
        sudo('supervisorctl status')