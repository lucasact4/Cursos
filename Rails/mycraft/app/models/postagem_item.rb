class PostagemItem < ApplicationRecord
  self.table_name = "postagem_itens"
  belongs_to :item
  belongs_to :postagem
end