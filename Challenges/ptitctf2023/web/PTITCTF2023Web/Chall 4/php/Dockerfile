FROM php:7.3-apache
COPY php.ini /usr/local/etc/php/
RUN apt-get update \
  && apt-get install -y --force-yes libfreetype6-dev libjpeg62-turbo-dev libpng-dev libmcrypt-dev\
  && docker-php-ext-install pdo_mysql mysqli mbstring gd iconv
RUN rm -rf /var/lib/apt/lists/* /tmp/*
