class User < SitePrism::Page
  set_url 'inscricao'
  element :nome, '#'
  element :sobrenome, '#'
  element :email, '#'
  element :endereco, '#'
  element :universidade, '#'
  element :profissao, '#'
  element :genero, '#'
  element :idade, '#'

  element :criar, 'input[value="Criar"]'

  def preencher_usuario
    nome.set 'bruno'
    sobrenome.set 'batista'
    email.set 'bruno@gmail.com'
    endereco.set 'rua 2'
    universidade.set 'anhanguera'
    profissao.set 'analista'
    genero.set 'Masculino'
    idade.set '28'
    criar.click
  end
end