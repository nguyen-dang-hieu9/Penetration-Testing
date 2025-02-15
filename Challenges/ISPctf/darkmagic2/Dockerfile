FROM ubuntu:20.04

# add user clownking
RUN useradd -m -s /bin/bash clownking


RUN apt-get update
RUN apt-get install python3 -y
RUN apt-get install python3-pip -y
RUN apt-get install vim -y
RUN apt-get install wget -y
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb
# RUN apt-get install -f -y
ENV TZ=Europe/Moscow
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# RUN apt-get install gconf-service -y
RUN apt-get install -f ./google-chrome-stable_current_amd64.deb -y

COPY requirements.txt requirements.txt
COPY chromedriver chromedriver
RUN chmod +x chromedriver
RUN pip3 install -r requirements.txt
# USER clownking

ENV FLAG=KCSC{FAKE_FLAG}
WORKDIR /app

EXPOSE 5001

CMD [ "python3", "main.py" ]