class ApplicationController < ActionController::Base
  protect_from_forgery with: :exception

  helper_method :current_jogador, :logged_in?

  def current_jogador
    @current_jogador ||= Jogador.find(session[:jogador_id]) if session[:jogador_id]
  end

  def logged_in?
    !!current_jogador
  end

  def require_user
    if !logged_in?
      flash[:danger] = "Você deve estar logado para executar essa ação!"
      redirect_to root_path
    end
  end

end
