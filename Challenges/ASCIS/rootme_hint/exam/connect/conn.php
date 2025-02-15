<?php
$servername = "db";
$username = "hung";
$password = "Hung123@";
$database = "test";
// $servername = "localhost";
// $username = "root";
// $password = "";
// $database = "test";

$conn = mysqli_connect($servername, $username, $password, $database);

if (!$conn) {
    die("Kết nối đến cơ sở dữ liệu thất bại: " . mysqli_connect_error()); // hàm die() sẽ hiển thị thông báo và kết thúc chương trình và không thực thi các câu lệnh phía sau
}

?>
