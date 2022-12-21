<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Polimorfismo</title>
</head>
<body>
  <pre>
  <?php
  require_once 'Mamifero.php';
  require_once 'Lobo.php';
  require_once 'Cachorro.php';
  $m = new Mamifero();
  $a = new Lobo();
  $b = new Cachorro();

  $m->setPeso(5.70);
  $m->setIdade(8);
  $m->setMembros(4);
  $m->emitirSom();
  $a->emitirSom();
  $b->emitirSom();

  $b->reagirFrase("Olá");
  $b->reagirFrase("Vai Apanhar!");
  $b->reagirHora(11,45);
  $b->reagirHora(21,00);
  $b->reagirDono(true);
  $b->reagirDono(false);
  $b->reagirIdadePeso(2, 12.5);
  $b->reagirIdadePeso(17, 4.5);

  print_r($m);
  print_r($a);
  print_r($b);

  ?>
  </pre>
</body>
</html>