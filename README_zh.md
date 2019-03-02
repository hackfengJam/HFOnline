# HFOnline
「基于Django在线教育系统」

## 写在前面
Introduction-en is [here](./README.md) 

## 快速开始

### 环境
- linux/windows
- python 2.7
- mysql 5.6
- 邮件服务器（本系统使用[网易邮箱](https://mail.163.com)：SMTP 服务）

### 步骤
1. 执行命令:
<pre>
pip install -r requirements.txt
cp ./config/config.yaml.example ./config/config.yaml
</pre>
2. 编辑 config.yaml
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
3. 数据库迁移
<pre>
python manage.py makemigrations
python manage.py migrate
</pre>
4. 启动服务
<pre>
python manage.py runserver
</pre>

## 示例
示例在[这里](./readme_detail/hfonline_detail.md) 

## 常见的问题解答

问：如何开启网易邮箱：SMTP 服务？

答：网易帮助文档：[163邮箱如何开启POP3/SMTP/IMAP服务？](http://help.163.com/10/0312/13/61J0LI3200752CLQ.html)