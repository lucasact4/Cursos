class RenameChefAndRecipeColumnsInComments < ActiveRecord::Migration[7.0]
  def change
    rename_column :comentarios, :chef_id, :jogador_id
    rename_column :comentarios, :recipe_id, :postagem_id
  end
end