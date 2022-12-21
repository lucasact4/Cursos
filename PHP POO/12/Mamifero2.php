<?php
require_once 'Mamifero.php';
class Canguru extends Mamifero {
  public function usarBolsa() {
    echo "<p>Usando bolsa</p>";
  }
  public function locomover() {
    echo "<p>Saltando</p>";
  }
}
class Cachorro extends Mamifero {
  public function enterrarOsso() {
    echo "<p>Enterrando Osso</p>";
  }
  public function abanarRabo() {
    echo "<p>Abanando o Rabo</p>";
  }
}
?>