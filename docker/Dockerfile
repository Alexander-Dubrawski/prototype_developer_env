FROM ubuntu:latest
MAINTAINER Alexander Dubrawski "dubrawski.alexander@gmail.com"

ENV INFLUXDB_VERSION 1.7.10

ENV TZ=Europe/Berlin

RUN apt-get update && \
    apt-get upgrade -y

# Install utilities   
RUN apt-get -y install vim  && \
    apt-get -y install apt-utils 

# Install all packages for Pyenv
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install git \
    make \
    build-essential \
    python-dev \
    python-pip \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    curl
RUN apt-get -y install libffi-dev
RUN pip install --upgrade pip

# Install Pyenv
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
ENV HOME  /
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.8.2
RUN pyenv global 3.8.2

# Install pipenv
RUN apt-get -y install libpq-dev
RUN pip install pipenv
RUN apt-get install -y wget

# Install INfluxdb
RUN     wget -nv https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
            dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb && rm influxdb_${INFLUXDB_VERSION}_amd64.deb
