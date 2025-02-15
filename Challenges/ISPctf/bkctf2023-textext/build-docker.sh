#!/bin/bash
chal="${CHAL:-java-deser-luk6785}"
docker rm -f "$chal"
docker build --tag="$chal" .
docker run -p 1337:1337 --rm --name="${chal}" "${chal}"