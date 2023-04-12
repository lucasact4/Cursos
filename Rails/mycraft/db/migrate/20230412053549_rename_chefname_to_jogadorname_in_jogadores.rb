class RenameChefnameToJogadornameInJogadores < ActiveRecord::Migration[7.0]
  def change
    rename_column :jogadores, :chefname, :jogadorname
  end
end