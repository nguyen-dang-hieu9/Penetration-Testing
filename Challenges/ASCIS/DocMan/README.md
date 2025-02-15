# ASCIS 2024 Final Round
# Challenge name: DocMan
# Category: Web

# Note: Source code, along with all necessary files for Docker build and run, is provided to contestants.


- Edit the internet facing port (e.g 8000) via `ports` block in `docker-compose.yml` file.
- Edit the flag content in `flag.txt` file.

Install docker and docker compose, then run: 

```
docker-compose up -d
docker exec docman mkdir /var/www/html/files
docker exec docman chown www-data:www-data /var/www/html/files
docker exec docman chmod 755 /var/www/html/files
docker exec docman ls -al
```

