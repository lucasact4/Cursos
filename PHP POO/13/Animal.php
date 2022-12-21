<?php
abstract class Animal {
  protected $peso, $idade, $membros;
  public abstract function locomover();
  public abstract function alimentar();
  public abstract function emitirSom();
  public function getPeso() {
    return $this->peso;
  }
  public function getIdade() {
    return $this->idade;
  }
  public function getMembros() {
    return $this->membros;
  }
  public function setPeso($peso) {
    return $this->peso = $peso;
  }
  public function setIdade($idade) {
    return $this->idade = $idade;
  }
  public function setMembros($membros) {
    return $this->membros = $membros;
  }
}
?>