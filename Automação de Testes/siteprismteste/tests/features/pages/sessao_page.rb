class Sessao < SitePrism::Section
  element :youtube, 'a[href="https://www.youtube.com"]'
  element :medium, 'a[href="https://www.medium.com"]'
end

class Pagina < SitePrism::Page

  set_url ''
  section :navbar, Sessao, '.nav-wrapper.container'

end