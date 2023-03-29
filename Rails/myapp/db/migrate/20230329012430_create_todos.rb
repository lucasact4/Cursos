class CreateTodos < ActiveRecord::Migration[7.0]
  def change
    create_table :todos do |t|

      t.string :nome
      t.text :description

    end
  end
end
