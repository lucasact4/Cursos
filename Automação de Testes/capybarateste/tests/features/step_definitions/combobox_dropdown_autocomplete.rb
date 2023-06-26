Quando('interajo com dropdown e select') do
  visit ''
  find('.btn.dropdown-button').click
  find('#dropdown3').click
  select 'Chrome', from: 'dropdown'
  find('option[value="2"]').select_option
  sleep(1)
end

Quando('preencho o autocomplete') do
  visit ''
  find('#autocomplete-input').set 'Rio de Jane'
  find('ul', text: 'Rio de Janeiro').click
  sleep(1)
end