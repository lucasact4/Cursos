class Todo < ApplicationRecord
  validates :nome, presence: true
  validates :description, presence: true

  belongs_to :user
end