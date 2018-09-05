FROM python:3
ADD . /nameredis-feeder/
WORKDIR /nameredis-feeder
RUN pip3 install --upgrade pip
RUN pip3 install -r requirements.txt
RUN apt-get update
RUN apt-get install -y gettext nano
CMD ./feeder.py
