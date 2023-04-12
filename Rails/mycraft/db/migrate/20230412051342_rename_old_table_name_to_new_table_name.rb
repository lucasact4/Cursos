class RenameOldTableNameToNewTableName < ActiveRecord::Migration[7.0]
  def change
    rename_table :recipes, :postagens
    rename_table :chefs, :jogadores
    rename_table :ingredients, :itens
    rename_table :recipe_ingredients, :postagem_itens
    rename_table :comments, :comentarios
  end
end
