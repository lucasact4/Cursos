Quando('eu faco um upload de arquivo') do
  visit ''
  # attach_file('upload', 'F:\Documents\GitHub\Cursos\Automação de Testes\capybarateste\tests\features\download.jpeg', make_visible: true)

  @foto = File.join(Dir.pwd, 'features/download.jpeg')
  attach_file('upload', @foto, make_visible: true)
  sleep(2)
end