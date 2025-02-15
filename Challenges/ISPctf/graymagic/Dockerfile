FROM php:8.0-apache

COPY src /var/www/html/
RUN chmod 777 /var/www/html/fonts
COPY index /usr/lib/cgi-bin/index
RUN chmod 755 /usr/lib/cgi-bin/index
RUN ln -s /etc/apache2/mods-available/cgi.load /etc/apache2/mods-enabled/

RUN echo KCSC{FAKE_FLAG} > /flag_$(echo $RANDOM | md5sum | head -c 20)

EXPOSE 8000