module Helper
  def tirar_foto(nome_aquivo, resultado)
    caminho_arquivo = "report/screenshots/test_#{resultado}"
    foto = "#{caminho_arquivo}/#{nome_aquivo}.png"
    page.save_screenshot(foto)
    embed(foto, 'imagem/png', 'Clique aqui')
  end
end