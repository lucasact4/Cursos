<?php
abstract class Pessoa {
  protected $nome;
  protected $idade;
  protected $sexo;
  protected $experiencia;
  public function __construct($nome, $idade, $sexo) {
    $this->nome = $nome;
    $this->idade = $idade;
    $this->sexo = $sexo;
    $this->experiencia = 0;
  }
  protected function ganharExp($n) {
    $this->experiencia += $n;
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
  public function getExperiencia() {
    return $this->experiencia;
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
  public function setExperiencia($experiencia) {
    return $this->experiencia = $experiencia;
  }
}
?>