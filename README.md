# HFOnline
HFOnline 基于Django在线教育系统

## Venusoneday
中文文档在[这里](./README_zh.md) 

# Quickstart

## Environment
- linux/windows
- python 2.7
- mysql 5.6
- mail server (This system uses [Netease mailbox](https://mail.163.com) : STMP service)

## Step:

1. run command:
<pre>
pip install -r requirements.txt
cp ./config/config.yaml.example ./config/config.yaml
</pre>

2.  edit config.yaml
<pre>
mysql:
  database: 'hfonline'
  username: 'root'
  password: '123456'
  host: '127.0.0.1'
  port: 3306
  charset: 'utf8'

email:
  host: 'smtp.163.com'
  port: 25
  host_user: 'xxxx@163.com' # 你的邮箱
  host_password: 'xxxxxxxx' # 你的密码
  use_tls: "no"
  from: 'xxxx@163.com' # 你的邮箱
</pre>
3. run server
<pre>
python manage.py runserver
</pre>