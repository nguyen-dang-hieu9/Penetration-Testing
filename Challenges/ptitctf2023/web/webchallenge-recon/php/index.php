<?php
// flag
$flag="PTITCTF{101-r3Con-101}"; 
$fakeflag="h4des{fake-flag}";

if (isset($_COOKIE['token'])) {
    $token = $_COOKIE['token'];
    if ($token == "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4tZmFrZSJ9.VosP2cIRNQVsR1obQZymxIjqSMu1UeXlccT6fU7Goss") {     
        echo "<br>Flag here: ".$fakeflag;
    } elseif ($token =="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4tZmxhZyJ9.XRFmbxnsQ-ermvUqDyTeMFntnKoMwDNSNvyxt3aaT0o") {
    	echo "<br>Flag here: ".$flag;
    }else{
    	echo "Error!";
    }
} else{
if (isset($_POST['username']) && isset($_POST['password'])) {
    $username = $_POST['username'];
    $password = $_POST['password'];
    if ($username === "admin" && $password === "123456") {
        $token = "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJuYW1lIjoiYWRtaW4tZmFrZSJ9.VosP2cIRNQVsR1obQZymxIjqSMu1UeXlccT6fU7Goss";
        setcookie("token", $token, time() + 3600, "/");
        echo "Đăng nhập thành công!";
        echo "<br>Flag here: ".$fakeflag;
    } else {
        echo "Sai tên đăng nhập hoặc mật khẩu!";
    }
} else{
	?>
<!DOCTYPE html>
<html lang="en">
<head>
	<title>hackertiemnang.com.vn</title>
	<meta charset="UTF-8">
	<meta name="viewport" content="width=device-width, initial-scale=1">
<!--===============================================================================================-->	
	<link rel="icon" type="image/png" href="login_asset/images/icons/favicon.ico"/>
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/bootstrap/css/bootstrap.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/fonts/font-awesome-4.7.0/css/font-awesome.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/fonts/Linearicons-Free-v1.0.0/icon-font.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/animate/animate.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/css-hamburgers/hamburgers.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/animsition/css/animsition.min.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/select2/select2.min.css">
<!--===============================================================================================-->	
	<link rel="stylesheet" type="text/css" href="login_asset/vendor/daterangepicker/daterangepicker.css">
<!--===============================================================================================-->
	<link rel="stylesheet" type="text/css" href="login_asset/css/util.css">
	<link rel="stylesheet" type="text/css" href="login_asset/css/main.css">
<!--===============================================================================================-->
</head>
<body>
	



	<div class="limiter">
		<div class="container-login100" style="background-image: url('login_asset/images/bg-01.jpg');">
			<div class="wrap-login100 p-t-30 p-b-50">
				<span class="login100-form-title p-b-41">
					Account Login
				</span>
				<span style="color:#FF0080; font-size: large" class=" p-b-41">
					
				</span>
				<form method="POST" action="" class="login100-form validate-form p-b-33 p-t-5">

					<div class="wrap-input100 validate-input" data-validate = "Enter username">
						<input class="input100" type="text" name="username" placeholder="User name">
						<span class="focus-input100" data-placeholder="&#xe82a;"></span>
					</div>

					<div class="wrap-input100 validate-input" data-validate="Enter password">
						<input class="input100" type="password" name="password" placeholder="Password">
						<span class="focus-input100" data-placeholder="&#xe80f;"></span>
					</div>

					<div class="container-login100-form-btn m-t-32">
						<button class="login100-form-btn">
							Login
						</button>
					</div>

				</form>
			</div>
		</div>
	</div>
	

	<div id="dropDownSelect1"></div>
	
<!--===============================================================================================-->
	<script src="login_asset/vendor/jquery/jquery-3.2.1.min.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/vendor/animsition/js/animsition.min.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/vendor/bootstrap/js/popper.js"></script>
	<script src="login_asset/vendor/bootstrap/js/bootstrap.min.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/vendor/select2/select2.min.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/vendor/daterangepicker/moment.min.js"></script>
	<script src="login_asset/vendor/daterangepicker/daterangepicker.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/vendor/countdowntime/countdowntime.js"></script>
<!--===============================================================================================-->
	<script src="login_asset/js/main.js"></script>

</body>
</html>

<?php }}?>