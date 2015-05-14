<?php


$id= $_POST['numEmployer'];
require '../manager/autoload.inc.php';
$racine="";
$con = new DBFactory();
$db=$con->getMysqlConnexionWithPDO();
$manage= new EmployerManager($db);
$employer = $manage->get($id);


?>