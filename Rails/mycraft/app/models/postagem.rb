class Postagem < ApplicationRecord
  validates :name, presence: true
  validates :description, presence: true, length: { minimum: 5, maximum: 500 }
  belongs_to :jogador
  validates :jogador_id, presence: true
  default_scope -> { order(updated_at: :desc) }
  has_many :postagem_itens
  has_many :itens, through: :postagem_itens
  has_many :comentarios, dependent: :destroy
end