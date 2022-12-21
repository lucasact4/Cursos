<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Teste PHP</title>
</head>
<body>
  <pre>
  <?php
    require_once 'Caneta.php';
    $c1 = new Caneta("BIC", "Azul", 0.5);
    $c1->setModelo("BIC");
    // $c1->modelo = "NIC"; public
    $c1->setPonta('0.5');
    // $c1->ponta = 0.4; private
    var_dump($c1);
    print "Eu tenho uma caneta {$c1->getModelo()} de ponta {$c1->getPonta()}";
  ?>
  </pre>
</body>
</html>