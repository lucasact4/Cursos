<?php
class Pessoa {
  private $nome;
  private $idade;
  private $sexo;

  public function fazerAniv() {
    $this->idade++;
  }
  public function getNome() {
    return $this->nome;
  }
  public function getIdade() {
    return $this->idade;
  }
  public function getSexo() {
    return $this->sexo;
  }
  public function setNome($nome) {
    return $this->nome = $nome;
  }
  public function setIdade($idade) {
    return $this->idade = $idade;
  }
  public function setSexo($sexo) {
    return $this->sexo = $sexo;
  }
}
?>