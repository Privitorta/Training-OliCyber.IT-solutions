<?php

if (isset($_GET["s"])) {
  highlight_file("index.php");
  exit;
}

$flag = getenv("FLAG");

echo "
<html>
<body>
  <form>
  Input: <input name=input />
  </form>

  <a href='?s'>Sorgente disponibile qui</a>.<br/>
</body>
</html>
";

if (isset($_GET['input'])) {
  $user_input = $_GET['input'];
      
  if ($user_input == substr(md5($user_input), 0, 24)) {
    echo "Ce l'hai fatta! Ecco la flag: $flag";
  } else {
    echo "Nope nope nope";
  }
}