#!/bin/bash

# Đánh dấu flag.txt là immutable
chattr +i /root/flag.txt

# Khởi động Apache
apache2-foreground
