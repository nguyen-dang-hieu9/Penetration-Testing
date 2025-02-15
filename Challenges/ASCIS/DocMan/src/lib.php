<?php
function createGuid() {
    if (function_exists('com_create_guid') === true)
        return strtolower(str_replace("-", "", trim(com_create_guid(), '{}')));
    return strtolower(sprintf('%04X%04X%04X%04X%04X%04X%04X%04X', mt_rand(0, 65535), mt_rand(0, 65535), mt_rand(0, 65535), mt_rand(16384, 20479), mt_rand(32768, 49151), mt_rand(0, 65535), mt_rand(0, 65535), mt_rand(0, 65535)));
}
function checkFileName($name) {
	return preg_match("/\.(docx|pdf)$/", strtolower($name));
}
function checkFileType($type) {
	return preg_match("/^(application\/vnd\.openxmlformats\-officedocument\.wordprocessingml\.document|application\/pdf)$/", strtolower($type));
}
function checkFileSize($size) {
	return ($size >= 1000 && $size <= 100000 ? true : false);
}
function checkFileMagic($fn) {
	$handle = fopen($fn, 'r');
    $magic = strtoupper(bin2hex(fread($handle, 8)));
    fclose($handle);
	return ($magic == "504B030414000600" || substr($magic, 0, 8)  == "25504446");
}
function sanitizeFileName($fn) {
	return preg_replace("/[\s]/", "-", preg_replace("/[\<\'\|\$\_\&\#\.\/\>]/", "", escapeshellarg($fn)));
}