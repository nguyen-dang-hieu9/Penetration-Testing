FROM php:7.4-apache

COPY my-apache2.conf /etc/apache2/apach2.conf
RUN a2enmod rewrite

WORKDIR /var/www/html

RUN apt update && apt upgrade -y

EXPOSE 80