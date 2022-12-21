<?php
class Pessoa {
  private $nome;
  private $idade;
  private $sexo;

  public function fazerAniver() {
    $this->idade++;
  }

  function __construct($nome, $idade, $sexo) {
    $this->nome = $nome;
    $this->idade = $idade;
    $this->sexo = $sexo;
  }

  function getNome() {
    return $this->nome;
  }
  function getIdade() {
    return $this->idade;
  }
  function getSexo() {
    return $this->sexo;
  }

  function setNome($nome) {
    return $this->nome = $nome;
  }
  function setIdade($idade) {
    return $this->idade = $idade;
  }
  function setSexo($sexo) {
    return $this->sexo = $sexo;
  }

}
?>