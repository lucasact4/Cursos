<?php
require_once 'Pessoa.php';
class Funcionario extends Pessoa {
  private $setor;
  private $trabalhando;
  public function mudarTrabalho() {
    return $this->trabalhando = ! $this->trabalhando;
  }
  public function getSetor() {
    return $this->setor;
  }
  public function getTrabalhando() {
    return $this->trabalhando;
  }
  public function setSetor($setor) {
    return $this->setor = $setor;
  }
  public function setTrabalhando($trabalhando) {
    return $this->trabalhando = $trabalhando;
  }
}
?>