<?php
require_once 'Pessoa.php';
require_once 'Publicacao.php';
class Livro implements Publicacao {
  private $titulo;
  private $autor;
  private $totPaginas;
  private $pagAtual;
  private $aberto;
  private $leitor;

  public function detalhes() {
    echo "<hr> Livro " . $this->titulo . " escrito por " . $this->autor;
    echo "<br> Páginas: " . $this->totPaginas . " atual " . $this->pagAtual;
    echo "<br> Sendo lido por " . $this->leitor->getNome();
  }

  function __construct($titulo, $autor, $totPaginas, $leitor) {
    $this->titulo = $titulo;
    $this->autor = $autor;
    $this->totPaginas = $totPaginas;
    $this->aberto = false;
    $this->pagAtual = 0;
    $this->leitor = $leitor;
  }

  public function getTitulo(){
    return $this->titulo;
  }
  public function getAutor(){
    return $this->autor;
  }
  public function getTotPaginas(){
    return $this->totPaginas;
  }
  public function getPagAtual(){
    return $this->pagAtual;
  }
  public function getAberto(){
    return $this->aberto;
  }
  public function getLeitor(){
    return $this->leitor;
  }

  public function setTitulo($titulo){
    return $this->titulo = $titulo;
  }
  public function setAutor($autor){
    return $this->autor = $autor;
  }
  public function setTotPaginas($totPaginas){
    return $this->totPaginas = $totPaginas;
  }
  public function setPagAtual($pagAtual){
    return $this->pagAtual = $pagAtual;
  }
  public function setAberto($aberto){
    return $this->aberto = $aberto;
  }
  public function setLeitor(){
    return $this->leitor;
  }

	public function abrir() {
    $this->aberto = true;
	}
	
	public function fechar() {
    $this->aberto = false;
	}
	
	public function folhear($p) {
    if($p>$this->totPaginas) {
      $this->pagAtual = 0;
    } else {
      $this->pagAtual = $p;
    }
	}
	
	public function avancarPag() {
    $this->pagAtual ++;
	}
	
	public function voltarPag() {
    $this->pagAtual --;
	}
}
?>