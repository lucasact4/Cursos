Quando('acesso a url') do
  @test = 1 + 1
  puts @test
  visit('')
  sleep(1)
end

Então('eu verifico se estou na pagina correta') do
  expect(page).to have_current_path('')
end