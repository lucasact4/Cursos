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
  require_once 'Mamifero2.php';
  $m = new Mamifero();
  $c = new Canguru();
  $k = new Cachorro();

  $m->setPeso(5.70);
  $m->setIdade(8);
  $m->setMembros(4);
  $m->locomover();
  $m->alimentar();
  $m->emitirSom();
  
  $c->setPeso(55.30);
  $c->setIdade(3);
  $c->setMembros(4);
  $c->locomover();
  $c->alimentar();
  $c->emitirSom();
  $c->usarBolsa();
  
  $k->setPeso(3.94);
  $k->setIdade(5);
  $k->setMembros(4);
  $k->locomover();
  $k->alimentar();
  $k->emitirSom();
  $k->abanarRabo();

  print_r($m);
  print_r($c);
  print_r($k);

  ?>
  </pre>
</body>
</html>