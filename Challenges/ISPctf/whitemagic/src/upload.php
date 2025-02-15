<?php
    function bodyguard($extension, $whitelist){
        if (in_array($extension, $whitelist)){
            return true;
        }
        else{
            return false;
        }
    }

    function isImg($extension){
        if ($extension == "jpg" || $extension == "jpeg" || $extension == "png" || $extension == "gif"){
            return true;
        }
        else{
            return false;
        }

    }

    function unzipFile($file){
        $zip = new ZipArchive;
        $res = $zip->open($file);
        if ($res === TRUE) {
            $zip->extractTo('upload/zip/unzipped');
            $zip->close();
            return true;
        } else {
            return false;
        }
    }

    function copyfile($path, $filename){
        $destination = "upload/images/".$filename;
        if (copy($path."/".$filename, $destination)){
            return true;
        }
        else{
            return false;
        }
    }

    function getFileinPath($path){
        $files = array_diff(scandir($path), array('..', '.'));

        foreach ($files as $key => $value) {
            // get file extension
            $extension = pathinfo($value, PATHINFO_EXTENSION);
            if (isImg($extension)){
                if(!copyfile($path, $value)){
                    die("Error: copy file failed");
                    exit();
                }
            }
            // delete file
            unlink($path ."/". $value);
        }
    }


    
    $whitelist_extension = ['jpg', 'jpeg', 'png', 'gif','zip'];
    // upload file
    $upload_dir = 'upload/';
    $file = $_FILES['file2upload'];
    // check empty file
    if (empty($file['name'])){
        echo "Error: empty file<br />";
    }
    $filename = basename($file['name']);
    $ext = pathinfo($filename, PATHINFO_EXTENSION);
    if (bodyguard($ext, $whitelist_extension)){
        if(isImg($ext)){
            $upload_file = $upload_dir . "images/" . basename($file['name']);
            if (move_uploaded_file($file['tmp_name'], $upload_file)){
                echo "File uploaded.\n";
            }
        }
        else{
            $upload_file = $upload_dir . "zip/" . basename($file['name']);
            if (move_uploaded_file($file['tmp_name'], $upload_file)){
                echo "File uploaded.\n";
            }
            if (unzipFile($upload_file)){
                getFileinPath($upload_dir . "zip/unzipped");
            }
            else{
                die("Error unzipping file.");
                exit();
            }
        }
    }
echo "Back to <a href='index.php'>Home</a>";
?>