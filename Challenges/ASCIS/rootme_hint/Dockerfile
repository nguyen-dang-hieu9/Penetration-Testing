# Sử dụng image PHP chính thức với Apache
FROM php:8.1-apache

# Cài đặt các extension cần thiết, ví dụ như mysqli để kết nối MySQL
RUN docker-php-ext-install mysqli pdo pdo_mysql

# Cài đặt sudo
RUN apt-get update && apt-get install -y sudo

# Cài đặt Python 3 và pip
RUN apt-get update && apt-get install -y python3 python3-pip

# Copy mã nguồn PHP của bạn vào thư mục /var/www/html (trừ các file bị loại trừ trong .dockerignore)
COPY ./exam /var/www/html/

# Tạo file php.ini với cấu hình tối ưu
RUN echo "upload_max_filesize = 7M\npost_max_size = 9M\nmax_execution_time = 300\nmax_input_time = 300" > /usr/local/etc/php/conf.d/uploads.ini

# Đảm bảo thư mục uploads có quyền ghi
RUN chmod -R 777 /var/www/html/uploads && echo "www-data ALL=(ALL) NOPASSWD: ALL" >> /etc/sudoers

# Mở cổng 80
EXPOSE 80

# Khởi động Apache
CMD ["apache2-foreground"]
