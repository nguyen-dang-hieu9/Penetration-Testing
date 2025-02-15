#!/bin/bash
echo "configuring webchallenge-recon on port 8011...";
docker build -t webchallenge-recon .;
docker run -d -p 8011:80 webchallenge-recon;