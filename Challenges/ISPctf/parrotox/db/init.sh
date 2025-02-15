#!/bin/bash
USER="fword"
PASSWORD="L33tPassW0rdF0rTesTiNgAround"

echo "Creating new user ${MYSQL_USER} ..."
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "CREATE USER '${USER}'@'%' IDENTIFIED BY '${PASSWORD}';"
echo "Granting privileges..."
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "GRANT ALL PRIVILEGES ON *.* TO '${USER}'@'%';"
mariadb -uroot -p$MYSQL_ROOT_PASSWORD -e "FLUSH PRIVILEGES;"
echo "All done."
