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
RUN pip3 install -r requirements.txt
# USER clownking

ENV FLAG=KCSC{p3wp3wp3w_Smash_Th3_Dimension}
WORKDIR /app

EXPOSE 8888

CMD [ "python3", "main.py" ]