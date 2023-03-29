class Todo < ApplicationRecord
  validates :nome, presence: true
end