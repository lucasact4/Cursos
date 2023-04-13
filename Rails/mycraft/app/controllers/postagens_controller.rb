class PostagensController < ApplicationController
  before_action :set_postagem, only: [:show, :update, :destroy]
  before_action :set_error, only: [:new, :edit]
  before_action :require_player, except: [:index, :show]
  before_action :require_same_player, only: [:edit, :update, :destroy]

  def index
    I18n.locale = 'pt'
    @postagens = Postagem.paginate(page: params[:page], per_page: 5)
  end

  def show
    @commentario = Comentario.new
    @comentarios = @postagem.comentarios.paginate(page: params[:page], per_page: 5)
  end

  def new
  end

  def create
    @postagem = Postagem.new(postagem_itens)
    @postagem.jogador = current_jogador
    if @postagem.save
      flash[:success] = "A postagem foi criada com sucesso!"
      redirect_to postagem_path(@postagem)
    else
      if @postagem.errors.any?
        @errors = true
        @count = @postagem.errors.count
        @error = @postagem.errors.messages
      end
      redirect_to new_postagem_path(postagem: @postagem, errors: @errors, count: @count, error: @error)
    end
  end

  def edit
    @postagem = Postagem.find(params[:id]) if params[:id]
  end

  def update
    if @postagem.update(postagem_itens)
      flash[:success] = "A postagem foi atualizada com sucesso!"
      redirect_to postagem_path(@postagem)
    else
      if @postagem.errors.any?
        @errors = true
        @count = @postagem.errors.count
        @error = @postagem.errors.messages
      end
      redirect_to edit_postagem_path(postagem: @postagem, errors: @errors, count: @count, error: @error)
    end
  end

  def destroy
    Postagem.find(params[:id]).destroy
    flash[:success] = "Postagem excluída com sucesso!"
    redirect_to postagens_path
  end

  private

    def set_postagem
      @postagem = Postagem.find(params[:id])
    end

    def set_error
      @error = params[:error]
      @count = params[:count]
      @errors = params[:errors] == 'true'
      @postagem = params[:postagem] || Postagem.new
    end
  
    def postagem_itens
      params.require(:postagem).permit(:name, :description, item_ids: [])
    end

    def require_same_player
      @postagem = Postagem.find(params[:id])
      if current_jogador != @postagem.jogador and !current_jogador.admin?
        flash[:danger] = "Você só pode editar ou excluir suas próprias postagens!"
        redirect_to postagens_path
      end
    end

end
