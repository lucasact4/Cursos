Quando('clico em botoes') do
  visit '/'
  click_on('Começar Automação') #click_link_or_button são identicos
  visit ''
  click_button(class: 'btn waves-light')
  find('a[onclick="ativaedesativa2()"]').click
  find('a[onclick="ativaedesativa2()"]').double_click
  find('a[onclick="ativaedesativa3()"]').right_click
  sleep(1)
  visit '/'
  click_link('Github')
end