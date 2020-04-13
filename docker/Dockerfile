FROM ubuntu:latest

ENV TZ=Europe/Berlin
ARG DEBIAN_FRONTEND=noninteractive
RUN apt-get update && \
    apt-get upgrade -y
RUN apt-get update

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
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
ENV HOME  /
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install 3.8.2
RUN pyenv global 3.8.2

RUN pip install --upgrade pip

RUN apt-get -y install libpq-dev

RUN pip install pipenv

