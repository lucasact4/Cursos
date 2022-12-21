<?php
class Lutador {
  private $nome;
  private $nacionalidade;
  private $idade;
  private $altura;
  private $peso;
  private $categoria;
  private $vitorias;
  private $derrotas;
  private $empates;
  public function __construct($nome, $nacionalidade, $idade, $altura, $peso, $vitorias, $derrotas, $empates) {
    $this->nome = $nome;
    $this->nacionalidade = $nacionalidade;
    $this->idade = $idade;
    $this->altura = $altura;
    $this->setPeso($peso);
    $this->vitorias = $vitorias;
    $this->derrotas = $derrotas;
    $this->empates = $empates;
  }
  public function apresentar() {
    echo "<p>--------------------------------</p>";
    echo "<p>CHEGOU A HORA! O Lutador {$this->getNome()} " ;
    echo "veio diretamente do país da(o) {$this->getNacionalidade()} ";
    echo "tem {$this->getIdade()} anos e pesa {$this->getPeso()}Kg ";
    echo "<br>Ele tem {$this->getVitorias()} vitória(s) ";
    echo "{$this->getDerrotas()} derrota(s) e {$this->getEmpates()} empate(s)!</p>";
  }
  public function status() {
    echo "<p>--------------------------------</p>";
    echo "<p>{$this->getNome()} é um peso {$this->getCategoria()} ";
    echo "e já ganhou {$this->getVitorias()} vez(es), ";
    echo "perdeu {$this->getDerrotas()} vez(es), ";
    echo "empatou {$this->getEmpates()} vez(es)!</p>";
  }
  public function ganharLuta() {
    $this->setVitorias($this->getVitorias() + 1);
  }
  public function perderLuta() {
    $this->setDerrotas($this->getDerrotas() + 1);
  }
  public function empatarLuta() {
    $this->setEmpates($this->getEmpates() + 1);
  }
  public function getNome() {
    return $this->nome;
  }
  public function getNacionalidade() {
    return $this->nacionalidade;
  }
  public function getIdade() {
    return $this->idade;
  }
  public function getAltura() {
    return $this->altura;
  }
  public function getPeso() {
    return $this->peso;
  }
  public function getCategoria() {
    return $this->categoria;
  }
  public function getVitorias() {
    return $this->vitorias;
  }
  public function getDerrotas() {
    return $this->derrotas;
  }
  public function getEmpates() {
    return $this->empates;
  }
  public function setNome($nome) {
    return $this->nome = $nome;
  }
  public function setNacionalidade($nacionalidade) {

  }
  public function setIdade($idade) {
    return $this->idade = $idade;
  }
  public function setAltura($altura) {
    return $this->altura = $altura;
  }
  public function setPeso($peso) {
    $this->setCategoria($peso);
    return $this->peso = $peso;
  }
  private function setCategoria($peso) {
    if ($peso < 52.2) {
      return $this->categoria = "Inválido";
    } elseif ($peso <= 70.3) {
      return $this->categoria = "Leve";
    } elseif ($peso <= 83.9) {
      return $this->categoria = "Médio";
    } elseif ($peso <= 120.2) {
      return $this->categoria = "Pesado";
    } else {
      return $this->categoria = "Inválido";
    }
  }
  public function setVitorias($vitorias) {
    return $this->vitorias = $vitorias;
  }
  public function setDerrotas($derrotas) {
    return $this->derrotas = $derrotas;
  }
  public function setEmpates($empates) {
    return $this->empates = $empates;
  }
}
?>