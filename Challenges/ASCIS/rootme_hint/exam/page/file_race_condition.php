<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Upload File</title>
</head>
<body>
    <h2>Upload a File</h2>
    <?php
     session_start();
     if ($_SERVER['REQUEST_METHOD'] == 'POST') {
        $target_dir = "../uploads/";
        $user_session = $_SESSION['user_id'];

        $target_file = $target_dir .$user_session.'_'. basename($_FILES["file"]["name"]);
        $uploadOk = 1;
        

        // Move file to target directory without checks
        if (move_uploaded_file($_FILES["file"]["tmp_name"], $target_file)) {
            // Introduce a delay (simulating a potential race condition window)
            //sleep(2);

            // Check MIME type and file type
            if (checkmime($target_file) && checkFileType($target_file)) {
                echo "The file ". htmlspecialchars($target_file). " has been uploaded.<br>";
                echo "The file is stored in " . $target_file . "<br>";
                //echo "<img src='$target_file' alt='Uploaded Image' style='max-width: 100%; height: auto;'><br>";
            } else {
                unlink($target_file);
                echo "Sorry, there was an error uploading your file.<br>";
                http_response_code(403);
            }
        } else {
            //echo "Sorry, there was an error moving your file.<br>";
        }
    }

    function checkmime($fileName) {
        $finfo = finfo_open(FILEINFO_MIME_TYPE);
        $mime_type = finfo_file($finfo, $fileName);
        $whitelist = array("image/jpeg", "image/png", "image/gif");
        finfo_close($finfo);
        if (!in_array($mime_type, $whitelist, TRUE)) {
            return false;
        } else {
            return true;
        }
    }

    function checkFileType($fileName) {
        $imageFileType = strtolower(pathinfo($fileName, PATHINFO_EXTENSION));
        if ($imageFileType != "jpg" && $imageFileType != "png" && $imageFileType != "jpeg" && $imageFileType != "gif") {
            echo "Sorry, only JPG, JPEG, PNG & GIF files are allowed.<br>";
            return false;
        } else {
            return true;
        }
    }
    ?>
    <form action="" method="post" enctype="multipart/form-data">
        <label for="file">Choose file to upload:</label>
        <input type="file" name="file" id="file">
        <input type="submit" value="Upload File" name="submit">
    </form>

   
        <h3>Uploaded Image:</h3>
        <img src="<?php echo htmlspecialchars($target_file); ?>" alt="Uploaded Image" style="max-width: 100%; height: auto;">
     
</body>
</html>
