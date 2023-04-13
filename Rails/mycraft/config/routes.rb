Rails.application.routes.draw do
  root "pages#home"
  get 'pages/home', to: 'pages#home'
  
  resources :postagens do
    resources :comentarios, only: [:create]
  end

  get '/signup', to: 'jogadores#new'
  resources :jogadores, except: [:new]

  get '/login', to: 'sessions#new'
  post '/login', to: 'sessions#create'
  delete '/logout', to: 'sessions#destroy'

  resources :itens, as: 'items'

end
