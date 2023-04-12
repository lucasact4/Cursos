class Comentario < ApplicationRecord
  validates :description, presence: true, length: { minimum: 4, maximum: 140 }
  belongs_to :jogador
  belongs_to :postagem
  validates :jogador_id, presence: true
  validates :postagem_id, presence: true
  default_scope -> { order(updated_at: :desc) }
end