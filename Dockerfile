FROM python:2.7.10

Label maitainer "hackfunjiang@163.com"

RUN mkdir -p /root/workspaces/ProgramFiles/Py2Code/HFOnline
RUN mkdir /root/workspaces/logs

ADD . /root/workspaces/ProgramFiles/Py2Code/HFOnline/HFOnline/

WORKDIR /root/workspaces/ProgramFiles/Py2Code/HFOnline/HFOnline
RUN pip install -i https://mirrors.aliyun.com/pypi/simple/ -r /root/workspaces/ProgramFiles/Py2Code/HFOnline/requirements.txt
