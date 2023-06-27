Quando('acesso a url') do
  @home = PaginaInicial.new
  @home.load
  sleep(2)
end

Então('verifico se estou na página inicial') do
  expect(page).to have_current_path('', url: true)
end