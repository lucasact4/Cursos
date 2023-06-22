=begin
module ModuloNome
  # Serve para agrupar classes
  # Serve para agrupar constantes
  # Serve para agrupar metódos
  # Ele é muito parecido com classe
  # Ele não pode ser instanciado
  # Módulo não pode ser herdado
  def metodo_padrao
    puts 'Eu sou um modulo'
  end
end

class ClassName
  include ModuloNome
end

object = ClassName.new

object.metodo_padrao
=end

class Cachorro
  def latir
    puts 'Au Au Au'
  end
end

class CachorroGrande
  def latir
    puts 'Au Au'
  end
end

class Pessoa
  def agarra_cachorro(cachorro)
    cachorro.latir
  end
end

c1 = Cachorro.new
c2 = CachorroGrande.new

p = Pessoa.new

p.agarra_cachorro(c1)
p.agarra_cachorro(c2)