class MapeandoElementoPage < SitePrism::Page
  set_url ''

  element :nome, ''

  def preencher
    nome.set 'bruno'
  end
end