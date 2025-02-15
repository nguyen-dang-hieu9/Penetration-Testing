<?php 

$servername = "database";
$username = "chall2";
$password = "asddva8439hefe4j";
$dbname = "anht0iCTF02";

$conn = new mysqli($servername, $username, $password, $dbname);

// Check connection
if ($conn->connect_error) {
  die("Connection failed: " . $conn->connect_error);
}
?>
