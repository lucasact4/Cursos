class PostagemItem < ApplicationRecord
  belongs_to :item
  belongs_to :postagem
end