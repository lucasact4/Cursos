<!DOCTYPE html>
<html lang="pt-br">
<head>
  <meta charset="UTF-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>Herança</title>
</head>
<body>
  <pre>
  <?php
  require_once 'Aluno.php';
  require_once 'Bolsista.php';
  require_once 'Professor.php';
  require_once 'Visitante.php';

  $p1 = new Visitante();
  $p2 = new Aluno();
  $p3 = new Professor();
  $p4 = new Bolsista();

  $p1->setNome("Pedro");
  $p2->setNome("Maria");
  $p3->setNome("Cláudio");
  
  $p1->setSexo("M");

  $p2->setCurso("Informática");
  $p3->setSalario("2500.75");

  $p3->receberAum(550.20);
  $p2->pagarMensalidade();

  $p4->setMatr(1112);
  $p4->setNome("Jubileu");
  $p4->setBolsa(12.5);
  $p4->setCurso("Administração");
  $p4->setIdade(17);
  $p4->pagarMensalidade();

  print_r($p1);
  print_r($p2);
  print_r($p3);
  print_r($p4);

  ?>
  </pre>
</body>
</html>