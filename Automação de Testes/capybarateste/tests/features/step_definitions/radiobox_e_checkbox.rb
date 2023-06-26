Quando('eu marco um checkbox e um radiobox') do
  visit ''
  find('labelfor="white"').click
  check('purple', allow_label_click: true)
  uncheck('purple', allow_label_click: true)
  sleep(1)
  choose('red', allow_label_click: true)
end