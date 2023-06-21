<?php
// Save this code in backend.php
$sharedContent = '';

if ($_SERVER['REQUEST_METHOD'] === 'POST') {
    $sharedContent = file_get_contents('php://input');
}

header('Content-Type: text/plain');
echo $sharedContent;
