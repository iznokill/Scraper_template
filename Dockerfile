FROM ubuntu:20.04

RUN apt-get update && apt-get install \
  -y --no-install-recommends python3 python3-virtualenv python3-pip python3-wheel python3-setuptools git python3-dev

RUN apt-get install -y --no-install-recommends autoconf automake libtool make curl

RUN apt-get install -y --no-install-recommends sudo


#------ START INSTALL CHROME --------
ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && apt-get install -y gnupg

RUN  apt-get update \
  && apt-get install -y wget \
  && rm -rf /var/lib/apt/lists/*


RUN sh -c 'echo "deb [arch=amd64] https://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'

RUN  wget -q -O - https://dl-ssl.google.com/linux/linux_signing_key.pub | sudo apt-key add -

RUN sudo apt-get update

RUN apt-get update -y

RUN apt-get install -y google-chrome-stable

#------ END INSTALL CHROME --------


ENV PYTHONPATH=/app:/app/.:/app/.

WORKDIR /app

COPY . .

RUN apt-get install -y locales && locale-gen en_US.UTF-8

RUN pip3 install -r requirements.txt

RUN locale-gen en_US.UTF-8
ENV LANG en_US.UTF-8
ENV LANGUAGE en_US:en
ENV LC_ALL en_US.UTF-8


ENTRYPOINT [ "python3" ]