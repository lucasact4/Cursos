Quando('eu entro na janela e verifico a mensagem') do
  visit ''

  #janela recebe uma janela que foi aberta pelo link
  janela = window_opened_by do
    click_link 'Clique aqui'
  end

  #muda de foco para a janela
  within_window janela do
    expect(current_url).to eq ''
    @mensagem = find('.red-text.text-darken-1.center')
    expect(@mensagem).to eq 'Você Abriu uma nova janela!!'
    janela.close
    sleep(1)
  end

  sleep(1)

  #segunda opção

  click_link 'Clique aqui'
  #mudando para ultima aba
  switch_to_window windows.last
  expect(current_url).to eq ''
  @mensagem = find('.red-text.text-darken-1.center')
  expect(@mensagem).to eq 'Você Abriu uma nova janela!!'
  windows.last.close

  sleep(1)

end

Quando('eu entro no alert e verifico faco a acao') do
  visit ''

  find('button[onclick="jsAlert()"]').click
  sleep(1)
  page.accept_alert
  sleep(1)

  find('button[onclick="jsConfirm()"]').click
  sleep(1)
  page.dismiss_confirm
  sleep(1)

  find('button[onclick="jsPrompt()"]').click
  sleep(1)
  page.accept_prompt(with: 'bruno batista')
  sleep(1)

  find('button[onclick="jsPrompt()"]').click
  page.dimiss_prompt
end