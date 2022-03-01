FROM dockerhub.hilton.com.cn/hilton/python:3.8-slim-ncat
COPY . /opt/webapp
WORKDIR /opt/webapp
RUN pip3 install --upgrade pip \
    && pip3 install -r requirements.txt --default-timeout=360 \
    && chmod a+x docker-entrypoint.sh
EXPOSE 5000
EXPOSE 5555
ENTRYPOINT [ "/opt/webapp/docker-entrypoint.sh" ]