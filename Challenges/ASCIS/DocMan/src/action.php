<?php
require_once("lib.php");
	
function fallback($p) {
	return "Page not found!";
}
function home($p) {
	return '
			<!DOCTYPE html><html><head>
				<meta charset="utf-8"/>
				<title>DocMan - Document Manager for Fun</title>
				<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
				<style type="text/css">
					body {padding:20px;}
					input[type=file] {display:none;}
					table {margin-top:30px;}
					span.err {color:red;}
				</style>
			</head><body>
				<h1>Your documents</h1>
				<p>Flag file: /var/www/data/flag.txt</p>
				<p>Note: Source code, along with all necessary files for Docker build and run, is provided to contestants.<p>
				<input type="file" accept=".docx,.pdf" required="required">
				<button class="btn btn-success">Upload DOCX or PDF</button>
				<span class="err"></span>
				<table class="table table-bordered"><thead>
					<tr><th>Name</th><th>Size</th>
				</thead><tbody></tbody></table>
				<script>
					document.querySelector("button").onclick = function() {
						document.querySelector("input[type=file]").click();
					};
					document.querySelector("input[type=file]").onchange = function() {
						if (this.value != "") {
							const file = this.files[0];
							const formData = new FormData();
							formData.append("newdoc", file);
							fetch("/", {
								method: "POST",
								body: formData
							}).then(resp => {
								resp.json().then(obj => {
									if (obj.err == "") {
										document.querySelector("span.err").textContent = "";
										let tr = document.createElement("tr");
										let td0 = document.createElement("td");
										let td1 = document.createElement("td");
										let a = document.createElement("a");
										a.textContent = file.name;
										a.href = "/g/" + encodeURIComponent(obj.givenName) + "." + file.name.split(".").pop();
										a.target = "_blank";
										td0.appendChild(a);
										td1.textContent = file.size.toString();
										tr.appendChild(td0);
										tr.appendChild(td1);
										document.querySelector("table tbody").appendChild(tr);
									} else {
										document.querySelector("span.err").textContent = translate(obj.err);
									}
								});
							});
						}		
					};
					function translate(err) {return ("Sorry: " + err);}
				</script>
			</body></html>';
}

function upload($p) {
	$file = $_FILES["newdoc"];
	$err = "";
	$givenName = "";
	if (!isset($file)) $err = "NO_FILE";
	else if (!checkFileName($file["name"])) $err = "FORBIDDEN_NAME";
	else if (!checkFileType($file["type"])) $err = "FORBIDDEN_TYPE";
	else if (!checkFileSize($file["size"])) $err = "FORBIDDEN_SIZE";
	else if (!checkFileMagic($file["tmp_name"])) $err = "FORBIDDEN_TYPE";
	if ($err == "") {
		$arr = explode(".", $file["name"]);
		$guid = createGuid();
		$givenName = sanitizeFileName($arr[0])."_".$guid;
		if (!move_uploaded_file($file["tmp_name"], "files/".$guid.".".sanitizeFileName($arr[1]))) {
			$err = "UPLOADING_ERROR";
			$givenName = "";
		}
	}
	return json_encode([
		"err" => $err, 
		"givenName" => $givenName
	]);
}

function viewOrDownload($p) {
	$f = explode("_", $p[0]);
	$fn = "files/".$f[1];
	if (file_exists($fn)) {
		$fp = @fopen($fn, "r");
		if (!$fp) {
			return "Document inaccessible!";
		} else {
			$data = fread($fp, filesize($fn));
			fclose($fp);
			header('Content-Type:'.mime_content_type($fn));
			return $data;
		}
	}
	return "Document not found!";
}