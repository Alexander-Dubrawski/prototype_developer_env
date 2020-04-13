FROM ubuntu:latest
MAINTAINER Alexander Dubrawski "dubrawski.alexander@gmail.com"

ENV INFLUXDB_VERSION 1.7.10
ENV PYTHON_VERSION 3.8.2
ENV USER_NAME ""
ENV USER_EMAIL ""
ENV HYRISE_BRANCH https://github.com/hyrise/hyrise.git
ENV CMAKE_VERSION 3.17
ENV CMAKE_BUILD 3.17.1

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

# Set up git 
RUN git config --global user.email ${USER_EMAIL} && \
    git config --global user.name ${USER_NAME}

# Install Pyenv
RUN git clone git://github.com/yyuu/pyenv.git .pyenv
RUN git clone https://github.com/yyuu/pyenv-virtualenv.git ~/.pyenv/plugins/pyenv-virtualenv
ENV HOME  /
ENV PYENV_ROOT $HOME/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH
RUN pyenv install ${PYTHON_VERSION}
RUN pyenv global ${PYTHON_VERSION}


# Set up locale-gen for pipenv 
RUN apt-get install -y locales
RUN locale-gen en_US.UTF-8

# Install pipenv
RUN apt-get -y install libpq-dev
RUN pip install --upgrade pip
RUN pip install pipenv
RUN apt-get install -y wget

# Install Influxdb
RUN     wget -nv https://dl.influxdata.com/influxdb/releases/influxdb_${INFLUXDB_VERSION}_amd64.deb && \
            dpkg -i influxdb_${INFLUXDB_VERSION}_amd64.deb && rm influxdb_${INFLUXDB_VERSION}_amd64.deb

# Install gcc 9
RUN apt -y install software-properties-common
RUN add-apt-repository ppa:ubuntu-toolchain-r/test
RUN apt -y install gcc-9 g++-9

RUN update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-9 60 --slave /usr/bin/g++ g++ /usr/bin/g++-9

# Install cmake
RUN mkdir ~/temp
RUN cd ~/temp && \
    wget https://cmake.org/files/v${CMAKE_VERSION}/cmake-${CMAKE_BUILD}.tar.gz && \
    tar -xzvf cmake-${CMAKE_BUILD}.tar.gz && \
    cd cmake-${CMAKE_BUILD} && \
    ./bootstrap && \
    make -j4 && \
    make install


# Install ninja 
RUN apt install ninja-build

# Install Hyrise 
RUN git clone --recursive ${HYRISE_BRANCH}

RUN apt-get install libncurses5-dev
RUN apt-get -y install libboost-all-dev
RUN DEBIAN_FRONTEND=noninteractive apt-get -y install postgresql
RUN apt-get -y install libpq-dev postgresql-server-dev-all
RUN apt-get -y install libtbb-dev


RUN rm /hyrise/install_dependencies.sh
ADD install_dependencies.sh hyrise/install_dependencies.sh
RUN ["chmod", "+x", "/hyrise/install_dependencies.sh"]
RUN mkdir /hyrise/cmake-build-release

RUN cd /hyrise/cmake-build-release && \
CXXFLAGS=-fdiagnostics-color=always cmake -DENABLE_NUMA_SUPPORT=Off -DCMAKE_BUILD_TYPE=Release -G Ninja ..
RUN cd /hyrise/cmake-build-release && ninja