# Classe começa com letra maiuscula
# Uma classe é composta por atributos, métodos e construtores
class ClassName
  
  # É a mesma coisa que o GET e SET do Java
  attr_accessor :nome

  # Só permite ler
  # attr_reader :nomeone

  # Só permite escrever
  # attr_writer :nometwo

=begin
  def nome
    @nome
  end

  def nome=(nome)
    @nome = :nome
  end
=end

  # Método
  # Nome dele tem que ser tudo minusculo
  # E se for nome composto tem que ter o _ entre as palavras
  def metodo
    #Corpo do método
    puts 'Corpo do método'
  end
  def metodo_composto
    #Corpo do método
    puts 'Corpo do método composto'
  end

end

class Heranca < ClassName

end

object = ClassName.new
object.nome = 'Brunão'
puts object.nome
object.metodo
object.metodo_composto

object_heranca = Heranca.new
object_heranca.metodo_composto