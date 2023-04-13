class ComentariosController < ApplicationController
  before_action :require_user

  def create
    @postagem = Postagem.find(params[:postagem_id])
    @comentario = @postagem.comentarios.build(comentario_params)
    @comentario.jogador = current_jogador

    if @comentario.save
      flash[:success] = "O comentário foi criado com sucesso"
      redirect_to postagem_path(@postagem)
    else
      flash[:danger] = "O comentário não foi criado"
      redirect_to postagem_path(@postagem)
    end
  end

  private

  def comentario_params
    params.require(:comentario).permit(:descricao)
  end
end