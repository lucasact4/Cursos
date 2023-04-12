class RenameColumnsInPostagemItens < ActiveRecord::Migration[7.0]
  def change
    rename_column :postagem_itens, :recipe_id, :postagem_id
    rename_column :postagem_itens, :ingredient_id, :item_id
  end
end