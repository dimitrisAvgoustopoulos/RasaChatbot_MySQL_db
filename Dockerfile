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

RUN --mount=type=secret,id=secret1 \
  --mount=type=secret,id=secret2 \
  --mount=type=secret,id=secret3 \
  --mount=type=secret,id=secret4 \
  --mount=type=secret,id=secret5 \
   export secret1=$(cat /run/secrets/secret1) && \
   export secret2=$(cat /run/secrets/secret2) && \
   export secret3=$(cat /run/secrets/secret3) && \
   export secret4=$(cat /run/secrets/secret4) && \
   export secret5=$(cat /run/secrets/secret5) && \
   yarn gen

ADD config.yml config.yml
ADD domain.yml domain.yml
ADD credentials.yml credentials.yml
ADD endpoints.yml endpoints.yml
