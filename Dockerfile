FROM centos:6

RUN yum install -y epel-release

RUN yum install -y python-pip python34 wget && wget https://bootstrap.pypa.io/get-pip.py

RUN python3.4 get-pip.py

RUN pip3.4 install hug requests

ADD server.py /opt/server.py

EXPOSE 8080

CMD hug -f /opt/server.py -ho 0.0.0.0 -p 8080
