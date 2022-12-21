<?php
require_once 'Animal.php';
class Ave extends Animal {
  private $corPena;
  public function locomover() {
    echo "<p>Voando</p>";
  }
  public function alimentar() {
    echo "<p>Comendo Alpiste</p>";
  }
  public function emitirSom() {
    echo "<p>Som de Ave</p>";
  }
  public function fazerNinho() {
    echo "<p>Construindo um ninho</p>";
  }
  public function getCorPena() {
    return $this->corPena;
  }
  public function setCorPena($corPena) {
    return $this->corPena = $corPena;
  }
}
?>