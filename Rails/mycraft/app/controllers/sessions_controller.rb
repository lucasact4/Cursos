class SessionsController < ApplicationController

  def new

  end

  def create
    chef = Chef.find_by(email: params[:session][:email].downcase)
    if chef && chef.authenticate(params[:session][:password])
      session[:chef_id] = chef.id
      flash[:success] = "Você fez login com sucesso!"
      redirect_to chef
    else
      redirect_to login_path, flash: { danger: "Há algo de errado com as informações de login digitadas!" }
    end
  end

  def destroy
    session[:chef_id] = nil
    flash[:success] = "Você deslogou!"
    redirect_to root_path
  end

end