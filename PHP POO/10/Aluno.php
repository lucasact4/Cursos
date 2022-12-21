<?php
require_once 'Pessoa.php';
class Aluno extends Pessoa {
  private $matr;
  private $curso;
  public function cancelarMatr() {
    echo "<p>Matrícula será cancelada</p>";
  }
  public function getMatr(){
    return $this->matr;
  }
  public function getCurso(){
    return $this->curso;
  }
  public function setMatr($matr){
    return $this->matr = $matr;
  }
  public function setCurso($curso){
    return $this->curso = $curso;
  }
}
?>