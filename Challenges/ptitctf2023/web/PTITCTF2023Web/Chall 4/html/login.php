<?php 
  if (isset($_SESSION['username'])){
      header("Location: index.php?page=home.php");
      header("Connection: close");
      exit;
    }
?>

<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
    <meta name="description" content="">
    <meta name="author" content="Mark Otto, Jacob Thornton, and Bootstrap contributors">
    <meta name="generator" content="Jekyll v4.1.1">
    <title>PTITCTF 2023</title>

    <link rel="canonical" href="https://getbootstrap.com/docs/4.5/examples/floating-labels/">

    <!-- Bootstrap core CSS -->
<link href="assets/dist/css/bootstrap.min.css" rel="stylesheet">

    <style>
      .bd-placeholder-img {
        font-size: 1.125rem;
        text-anchor: middle;
        -webkit-user-select: none;
        -moz-user-select: none;
        -ms-user-select: none;
        user-select: none;
      }

      @media (min-width: 768px) {
        .bd-placeholder-img-lg {
          font-size: 3.5rem;
        }
      }
    </style>
    <!-- Custom styles for this template -->
    <link href="floating-labels.css" rel="stylesheet">
  </head>
  <body>
    <form class="form-signin" method="POST" action="?page=login.php">
  <div class="text-center mb-4">
    <img class="mb-4" src="pis.jpg"  width="120" height="120">
    <h1 class="h3 mb-3 font-weight-normal">Login</h1>
    <p>Only for PIS member</a></p>
  </div>

  <div class="form-label-group">
    <input type="text" id="inputUsername" name="username" class="form-control" placeholder="Username" required autofocus>
    <label for="inputEmail">Username</label>
  </div>

  <div class="form-label-group">
    <input type="password" id="inputPassword" name="password" class="form-control" placeholder="Password" required>
    <label for="inputPassword">Password</label>
  </div>

  <div class="checkbox mb-3">
    <label>
       New user? <a href="?page=register.php">Register</a></br>
      <input type="checkbox" value="remember-me"> Remember me
    </label>
    <?php  
      if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])){
                        $username=$_POST['username'];
                        $password=$_POST['password'];
                        $stmt = $conn->prepare("SELECT * FROM user where username=? and password=?");
                        $stmt->bind_param("ss", $username, $password);
                        $stmt->execute();
                        $result = $stmt->get_result();
                        $user = $result->fetch_assoc(); 
                        if (empty($user)){
                            echo "<div class='alert alert-danger' role='alert'>
                            <strong>Username or password is incorrect</strong></div>";
                        }
                        else{
                            $query  = "SELECT SLEEP(1);"; // waiting to prevent error
                            $query .= "INSERT INTO log(username,time,browser) VALUES ('".$user['username']."',CURRENT_TIMESTAMP(),'".$_SERVER['HTTP_USER_AGENT']."')";
                            if ($conn->multi_query($query)) {
                              do {
                                 // nothing
                              } while ($stmt->next_result());
                            }

                            $_SESSION['username']=$user['username'];
                            header("Location: ?page=home.php");
                            header("Connection: close");
                            exit;
                        }
                    }

    ?>
  </div>
  <button class="btn btn-lg btn-primary btn-block" type="submit">Login</button>
  <p class="mt-5 mb-3 text-muted text-center">&copy; PTITCTF 2023</p>
</form>
</body>
</html>
