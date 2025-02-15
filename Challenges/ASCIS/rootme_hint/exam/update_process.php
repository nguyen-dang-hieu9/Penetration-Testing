<?php
session_start();

include './connect/conn.php';
if(!isset($_SESSION['user_id']) ){
    header("Location: login.php");
    die();
}

$user_id = $_SESSION['user_id'];

if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $fullName = htmlspecialchars($_POST['fullname']);
    $email = htmlspecialchars($_POST['email']);
    $address = htmlspecialchars($_POST['address']);
    $telephone = htmlspecialchars($_POST['telephone']);

    $target_dir = "uploads/";
    $user_session = $_SESSION['user_id'];

    $sql = "SELECT * FROM user WHERE id = ?";
    $stmt = $conn->prepare($sql);
    $stmt->bind_param("s", $user_id);
    $stmt->execute();
    $result = $stmt->get_result();
    $profilePicture = $result->fetch_assoc()['profile_picture'];

    $uploadOk = 1;

    if (isset($_FILES['file-upload']) && $_FILES['file-upload']['size'] > 0) {
        $target_file = $target_dir . $user_session . '_' . basename($_FILES["file-upload"]["name"]);
        move_uploaded_file($_FILES["file-upload"]["tmp_name"], $target_file);

        if (checkmime($target_file) && checkFileType($target_file)) {
            $profilePicture = $target_file;
        } else {
            unlink($target_file);
            http_response_code(403);
            $uploadOk = 0;
        }
    }

    if ($uploadOk) {
        $sql = "UPDATE user SET full_name = ?, email = ?, address = ?, telephone = ?, profile_picture = ? WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("ssssss", $fullName, $email, $address, $telephone, $profilePicture, $user_session);
        $stmt->execute();

        if ($stmt->affected_rows > 0) {
            header("Location: update.php");
            exit(); // Sử dụng exit() ngay sau header để đảm bảo script dừng lại.
        } else {
            echo "Cập nhật thông tin người dùng thất bại.";
        }
    } else {
        // Cập nhật các thông tin khác nếu ảnh không được tải lên thành công
        $sql = "UPDATE user SET full_name = ?, email = ?, address = ?, telephone = ? WHERE id = ?";
        $stmt = $conn->prepare($sql);
        $stmt->bind_param("sssss", $fullName, $email, $address, $telephone, $user_session);
        $stmt->execute();

        if ($stmt->affected_rows > 0) {
            header("Location: update.php");
            exit(); // Sử dụng exit() ngay sau header để đảm bảo script dừng lại.
        } else {
            echo "Cập nhật thông tin người dùng thất bại (không bao gồm ảnh).";
        }
    }
}

function checkmime($fileName) {
    $finfo = finfo_open(FILEINFO_MIME_TYPE);
    $mime_type = finfo_file($finfo, $fileName);
    $whitelist = array("image/jpeg", "image/png", "image/gif");
    finfo_close($finfo);
    return in_array($mime_type, $whitelist, true);
}

function checkFileType($fileName) {
    $imageFileType = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
    return in_array($imageFileType, array("jpg", "jpeg", "png", "gif"), true);
}
?>
