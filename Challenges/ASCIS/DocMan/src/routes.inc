<?php
	$routes = array(
		array("get", "/", "home"),
		array("post", "/", "upload"),
		array("get", "/g/{id}", "viewOrDownload")
	);