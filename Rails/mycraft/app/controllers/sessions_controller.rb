class SessionsController < ApplicationController

  def new

  end

  def create
    jogador = Jogador.find_by(email: params[:session][:email].downcase)
    if jogador && jogador.authenticate(params[:session][:password])
      session[:jogador_id] = jogador.id
      flash[:success] = "Você fez login com sucesso!"
      redirect_to jogadore_path(jogador)
    else
      redirect_to login_path, flash: { danger: "Há algo de errado com as informações de login digitadas!" }
    end
  end

  def destroy
    session[:jogador_id] = nil
    flash[:success] = "Você deslogou!"
    redirect_to root_path
  end

end