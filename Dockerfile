FROM python:3.7.3-stretch AS BASE

RUN apt-get update \
    && apt-get --assume-yes --no-install-recommends install \
        build-essential \
        curl \
        git \
        jq \
        libgomp1 \
        vim

WORKDIR /app

# upgrade pip version
RUN pip install --no-cache-dir --upgrade pip

RUN pip install rasa==3.1.0
RUN pip install mysql
RUN pip install mysql-connector
RUN pip install mysql-connector-python
RUN pip install sanic==21.12.1
RUN pip install Sanic-Cors==2.0.1
RUN pip install sanic-jwt==1.7.0
RUN pip install sanic-plugin-toolkit==1.2.1
RUN pip install sanic-routing==0.7.2

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
