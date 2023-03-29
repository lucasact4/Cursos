class Todo < ApplicationRecord
  validates :nome, presence: true
  validates :description, presence: true
end