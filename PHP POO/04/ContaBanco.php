<?php
class ContaBanco {
  // Atributos
  public $numConta;
  protected $tipo;
  private $dono;
  private $saldo;
  private $status;
  // Métodos
  public function abrirConta($t) {
    $this->setTipo($t);
    $this->setStatus(true);
    if ($t == "CC") {
      $this->setSaldo(50);
      echo "<p>Olá, {$this->getDono()}! Você abriu uma conta Corrente, então ganhou R$50,00!</p>";
    } elseif ($t == "CP") {
      $this->saldo = 150;
      echo "<p>Olá, {$this->getDono()}! Você abriu uma conta Poupança, então ganhou R$150,00!</p>";
    }
  }
  public function fecharConta() {
    if ($this->getSaldo() > 0) {
      echo "<p>Conta ainda tem dinheiro, não posso fechá-la!</p>";
    } elseif ($this->getSaldo() < 0) {
      echo "<p>Conta está em débito. Impossível encerrar!</p>";
    } else {
      $this->setStatus(false);
      echo "<p>Conta de ".$this->getDono()." fechada com sucesso!</p>";
    }
  }
  public function depositar($v) {
    if ($this->getStatus()) {
      $this->setSaldo($this->getSaldo() + $v);
      echo "<p>Depósito de R$$v na conta de ".$this->getDono()."!</p>";
    } else {
      echo "<p>Conta fechada. Não consigo depositar.</p>";
    }
  }
  public function sacar($v) {
    if ($this->getStatus()) {
      if ($this->getSaldo() >= $v) {
        $this->setSaldo($this->getSaldo() - $v);
        echo "<p>Saque de R$$v autorizado na conta de ".$this->getDono()."!</p>";
      } else {
        echo "<p>Saldo insuficiente para saque.</p>";
      }
    } else {
      echo "<p>Não posso sacar de uma conta fechada.</p>";
    }
  }
  public function pagarMensal() {
    if ($this->getTipo() == "CC") {
      $v = 12;
    } elseif ($this->getTipo() == "CP") {
      $v = 20;
    }
    if ($this->getStatus()) {
      $this->setSaldo($this->getSaldo() - $v);
      echo "<p>Mensalidade de R$$v debitada na conta de ".$this->getDono()."!</p>";
    } else {
      echo "<p>Problemas com a conta. Não posso cobrar.</p>";
    }
  }
  // Métodos Especiais
  public function __construct() {
    $this->setSaldo(0);
    $this->setStatus(false);
    echo "<p>Conta criada com sucesso!</p>";
  }
  public function getNumConta() {
    return $this->numConta;
  }
  public function getTipo() {
    return $this->tipo;
  }
  public function getDono() {
    return $this->dono;
  }
  public function getSaldo() {
    return $this->saldo;
  }
  public function getStatus() {
    return $this->status;
  }
  public function setNumConta($numConta) {
    return $this->numConta = $numConta;
  }
  public function setTipo($tipo) {
    return $this->tipo = $tipo;
  }
  public function setDono($dono) {
    return $this->dono = $dono;
  }
  public function setSaldo($saldo) {
    return $this->saldo = $saldo;
  }
  public function setStatus($status) {
    return $this->status = $status;
  }
}
?>