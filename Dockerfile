FROM python:2.7.10

Label maitainer "hackfunjiang@163.com"

RUN mkdir -p /config/HFOnline
RUN mkdir /config/logs

ADD . /config/HFOnline/

WORKDIR /config/HFOnline
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /config/HFOnline/requirements.txt
