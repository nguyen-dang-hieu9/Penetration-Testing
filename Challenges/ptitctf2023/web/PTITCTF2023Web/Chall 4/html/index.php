<?php 
	session_start();
	require("db.php");
	if (isset($_GET['page'])&&!empty($_GET['page'])){
		if (strpos($_GET['page'], ':')||!strpos($_GET['page'],".php")){
			die('Something was wrong');
		}
		else{
			$page=$_GET['page'];
			include($page);
		}	
	}
	else{
		include("login.php");
	}
?>
