FROM tomcat:9.0.70-jre8

RUN rm -rf /usr/local/tomcat/webapps/ROOT/
COPY flag.txt /flag.txt
COPY challenge/text.war /usr/local/tomcat/webapps/text.war
COPY config/tomcat-users.xml /usr/local/tomcat/conf/tomcat-users.xml

RUN sed -i 's|8080|1337|g' /usr/local/tomcat/conf/server.xml

CMD ["catalina.sh", "run"]

EXPOSE 1337
