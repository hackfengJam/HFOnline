FROM python:2.7.13

Label maitainer "fangzhou@jiagouyun.com"

RUN mkdir -p /config/cloudcare-backend
RUN mkdir /config/logs

ADD . /config/cloudcare-backend/

WORKDIR /config/cloudcare-backend
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /config/cloudcare-backend/requirements.txt
