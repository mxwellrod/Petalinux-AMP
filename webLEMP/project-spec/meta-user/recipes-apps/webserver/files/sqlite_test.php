<?php
// Simple HTML, PHP & SQLite example code that checks the basic operation of
// SQLite. SQL queries used are :-
//
// 1. Create/open database
// 1. Create table
// 3. Insert row
// 4. Close database
//
?>

<!DOCTYPE html>
<html lang="en">
<head>
<meta http-equiv="content-type" content="text/html; charset=UTF-8">
<title>SQLite Test</title>
</head>

<?php

echo 'Creating/opening database<br>';
$db = new SQLite3('/var/www/localhost/html/db/db1.db');
if ($db) {
  echo 'Success';
} else {
  echo 'Failure : ' . $db->lastErrorMsg();
}
echo '<br><br>';

echo 'Creating table<br>';
$return = $db->exec("CREATE TABLE IF NOT EXISTS fruit (item VARCHAR(30) NOT NULL PRIMARY KEY UNIQUE, quantity int unsigned NOT NULL)");
if ($return) {
  echo 'Success';
} else {
  echo 'Failure : ' . $db->lastErrorMsg();
}
echo '<br><br>';

echo 'Inserting 1st row in table<br>';
$result = $db->exec("INSERT INTO fruit (item, quantity) VALUES ('Manzana', '5')");
if ($result) {
  echo 'Success';
} else {
  echo 'Failure : ' . $db->lastErrorMsg();
}
echo '<br><br>';

echo 'Inserting 2nd row in table<br>';
$result = $db->exec("INSERT INTO fruit (item, quantity) VALUES ('Naranjas', '12')");
if ($result) {
  echo 'Success';
} else {
  echo 'Failure : ' . $db->lastErrorMsg();
}
echo '<br><br>';

echo 'Closing database<br>';
$result = $db->close();
if ($result) {
  echo 'Success';
} else {
  echo 'Failure : ' . $db->lastErrorMsg();
}

?>

</body>
</html>
