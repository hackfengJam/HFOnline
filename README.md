# HFOnline
「Online Education System Based on Django」

## Venusoneday
中文文档在[这里](./README_zh.md) 

# Quickstart

## Environment
- linux/windows
- python 2.7
- mysql 5.6
- mail server (This system uses [Netease mailbox](https://mail.163.com) : SMTP service)

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
3. db migration
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>
4. run server
<pre>
python manage.py runserver
</pre>

## Demo
demo is [here](./readme_detail/hfonline_detail.md) 

## FAQ
Q: How to open Netease mailbox SMTP service?

A: Netease help docs：[163邮箱如何开启POP3/SMTP/IMAP服务](http://help.163.com/10/0312/13/61J0LI3200752CLQ)