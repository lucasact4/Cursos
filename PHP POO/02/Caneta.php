<?php
class Caneta {
  public $modelo;
  public $cor;
  private $ponta;
  protected $carga;
  private $tampada;

  public function rabiscar() {
    if ($this->tampada == true) {
      echo "<p>ERRO! Não posso rabiscar!</p>";
    } else {
      echo "<p>Estou rabiscando...</p>";
    }
  }
  public function tampar() {
    $this->tampada = true;
    echo "<p>Caneta Tampada</p>";
  }
  protected function destampar() {
    $this->tampada = false;
    echo "<p>Caneta Destampada</p>";
  }
}
?>