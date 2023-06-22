puts 'Digite um número, 1 ou 2'
v1 = gets.to_i

=begin
if v1 == 1
  puts 'Valor igual a 1'
elsif v1 == 2
  puts 'Valor é igual a 2'
else
  puts 'Valor não é igual a 1'
end
=end

=begin
unless v1 == 2
  puts 'Condição falsa'
else
  puts 'Condição verdadeira'
end
=end

case v1
when 0
  puts 'Digitou 0'
when 1
  puts 'Digitou 1'
else
  puts 'Opção inválida'
end