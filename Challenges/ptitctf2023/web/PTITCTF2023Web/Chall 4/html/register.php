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
    <form class="form-signin" method="POST" action="?page=register.php">
  <div class="text-center mb-4">
    <img class="mb-4" src="pis.jpg"  width="120" height="120">
    <h1 class="h3 mb-3 font-weight-normal">Register</h1>
    <p>Only for PIS member</a></p>
  </div>

  <div class="form-label-group">
    <input type="text" id="inputEmail" name="username" class="form-control" placeholder="Email address" required autofocus>
    <label for="inputEmail">Username</label>
  </div>

  <div class="form-label-group">
    <input type="password" id="inputPassword" name="password" class="form-control" placeholder="Password" required>
    <label for="inputPassword">Password</label>
  </div>

  <div class="checkbox mb-3">
    <label>
      Have another account? <a href="?page=login.php">Login</a>
    </label>
    <?php
       if (isset($_POST['username'])&&!empty($_POST['username'])&&isset($_POST['password'])&&!empty($_POST['password'])){
                    $username=$_POST['username'];
                    $password=$_POST['password'];
                    if (strlen($username)<5||strlen($password)<7){
                       echo "<div class='alert alert-danger' role='alert'>
                            <strong>Invalid length</strong></div>";
                    }
                    else{
                        if (preg_match('/^([a-zA-Z]+)$/',$username)&&preg_match('/^([a-zA-Z]+)$/',$password)){
                              $stmt = $conn->prepare("SELECT * FROM user where username=?");
                              $stmt->bind_param("s", $username);
                              $stmt->execute();
                              $result = $stmt->get_result(); // get the mysqli result
                              $user = $result->fetch_assoc(); // fetch data   
                              if (!empty($user)){
                                echo "<div class='alert alert-danger' role='alert'>
                                    <strong>Username have already exists</strong></div>";
                              }
                              else{
                                  $stmt = $conn->prepare("INSERT into user VALUES (?,?)");
                                  $stmt->bind_param("ss", $username,$password);
                                  $stmt->execute();
                                  header("Location: index.php?page=login.php");
                                  header("Connection: close");
                                  exit;
                                }
                          }
                          else{
                             echo "<div class='alert alert-danger' role='alert'>
                            <strong>Allow only alphabet character</strong></div>";
                          } 
                     
                       }
                   
                      }
    ?>
  </div>
  <button class="btn btn-lg btn-primary btn-block" type="submit">Register</button>
  <p class="mt-5 mb-3 text-muted text-center">&copy; PTITCTF 2023</p>
</form>
</body>
</html>
