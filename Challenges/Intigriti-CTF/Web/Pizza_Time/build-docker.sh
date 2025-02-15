#!/bin/bash
docker rm -f web_pizza_time
docker build --tag=web_pizza_time .
docker run --cap-drop=CAP_SYS_ADMIN -p 1337:1337 --rm --name=web_pizza_time web_pizza_time