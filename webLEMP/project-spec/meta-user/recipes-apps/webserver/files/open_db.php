<?php
$db = new SQLite3('/var/www/localhost/html/open_test.db');
if($db) {
    echo "OK";
} else {
    echo "ERROR: " . $db->lastErrorMsg();
}
?>
