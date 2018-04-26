#!/usr/bin/env python
# -*- coding:utf-8 -*-
from __future__ import unicode_literals

__Author__ = "HackFun"

import pymysql

import os
import yaml
import json
import base64
import requests

pymysql.install_as_MySQLdb()

base_path = os.path.dirname(os.path.abspath(__file__))
print base_path
config = {}


def init_config():
    global config
    path = os.environ.get('CLOUDCARE_BACKEND_CONFIG')
    if path is None:
        with open(base_path + "/../config/config.yaml") as f:
            config = yaml.load(f)
    else:
        config = load_from_etcd(path)


def load_from_etcd(path):
    resp = requests.get(path)
    try:
        text = base64.b64decode(resp.json()['node']['value'])
    except:
        text = base64.b64decode(resp.json()['node']['value'].replece(' ', '+'))  # TODO 谭彪哥提醒
    return yaml.load(text)


init_config()
