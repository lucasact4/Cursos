class Item < ApplicationRecord
  validates :name, presence: true, length: { minimum: 3, maximum: 25 }
  validates_uniqueness_of :name
  has_many :postagem_itens
  has_many :postagens, through: :postagem_itens
end