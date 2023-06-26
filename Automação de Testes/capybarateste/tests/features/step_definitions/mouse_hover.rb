Quando('seleciono o mouse hover') do
  visit ''
  find('.activator').hover
  find('.activator').click
  sleep(1)
end