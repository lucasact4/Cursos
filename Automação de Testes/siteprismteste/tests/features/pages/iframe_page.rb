class PaginaIframe < SitePrism::Page
  element :nome, '#first_name'
  element :ultimo_nome, '#last_name'
end

class PaginaPadrao < SitePrism::page
  set_url ''
  iframe :preencher_campo, PaginaIframe, '#id_do_iframe'
end