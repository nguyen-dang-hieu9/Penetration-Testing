# ubuntu lastest version: 18.04
FROM php:8.0-apache

RUN apt-get update && apt-get upgrade -y
RUN apt-get install libzip-dev -y
RUN docker-php-ext-install zip
RUN useradd -m -s /bin/bash clownking
COPY flag.txt /flag.txt
RUN chmod 754 /flag.txt
USER clownking
WORKDIR /var/www/html