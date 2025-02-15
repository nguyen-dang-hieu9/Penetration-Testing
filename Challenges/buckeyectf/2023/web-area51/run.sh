#!/bin/bash
set -e
./build.sh
docker run --rm -p8081:80 -it area51
