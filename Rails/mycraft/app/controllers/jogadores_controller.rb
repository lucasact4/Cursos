class JogadoresController < ApplicationController
  before_action :set_jogador, only: [:show, :update, :destroy]
  before_action :set_error, only: [:new, :edit]
  before_action :require_same_user, only: [:edit, :update, :destroy]
  before_action :require_admin, only: [:destroy]

  def index
    @jogadores = Jogador.paginate(page: params[:page], per_page: 5)
  end

  def new
  end

  def create
    @jogador = Jogador.new(jogador_params)
    if @jogador.save
      session[:jogador_id] = @jogador.id
      flash[:success] = "Bem-vindo(a) #{@jogador} ao MyCraft Blog!"
      redirect_to jogador_path(@jogador)
    else
      if @jogador.errors.any?
        @errors = true
        @count = @jogador.errors.count
        @error = @jogador.errors.messages
      end
      redirect_to signup_path(jogador: @jogador, errors: @errors, count: @count, error: @error)
    end
  end

  def show
    @jogador_postagens = @jogador.postagens.paginate(page: params[:page], per_page: 5)
  end

  def edit
    @jogador = Jogador.find(params[:id]) if params[:id]
  end

  def update
    if @jogador.update(jogador_params)
      flash[:success] = "Sua conta foi atualizada com sucesso!"
      redirect_to @jogador
    else
      if @jogador.errors.any?
        @errors = true
        @count = @jogador.errors.count
        @error = @jogador.errors.messages
      end
      redirect_to edit_jogador_path(jogador: @jogador, errors: @errors, count: @count, error: @error)
    end
  end

  def destroy
    if !@jogador.admin?
      @jogador.destroy
      flash[:danger] = "Jogador e todas as postagens associadas foram deletadas!"
      redirect_to jogadores_path
    end
  end

  private

  def jogador_params
    params.require(:jogador).permit(:jogadorname, :email, :password, :password_confirmation)
  end

  def set_jogador
    @jogador = Jogador.find(params[:id])
  end

  def set_error
    @error = params[:error]
    @count = params[:count]
    @errors = params[:errors] == 'true'
    @jogador = params[:jogador] || Jogador.new
  end

  def require_same_user
    @jogador = Jogador.find(params[:id])
    if current_jogador != @jogador and !current_jogador.admin?
      flash[:danger] = "Você só pode editar ou excluir sua própria conta!"
      redirect_to jogadores_path
    end
  end

  def require_admin
    if logged_in? && !current_jogador.admin?
      flash[:danger] = "Somente jogadores administradores podem executar essa ação!"
      redirect_to root_path
    end
  end

end