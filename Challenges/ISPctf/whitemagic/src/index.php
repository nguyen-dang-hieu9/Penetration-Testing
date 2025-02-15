<html>
    <head>
        <title>Home</title>
    </head>

    <body>
        <a href="#">Home</a><?php echo "\t"?><a href="upload.html">Upload</a>
        <h1>List images</h1>
        <ul>
            <?php
                $files = array_diff(scandir("upload/images/"), array('..', '.'));
                foreach ($files as $file) {
                    echo "<li><a href='upload/images/$file'>$file</li>";
                }?>
        </ul>
    </body>
</html>