

v1 = 1
v2 = 2
v3 = 3
v4 = 4

if (v1 < v2) && (v3 < v4)
  puts "Condição atendida pelos dois casos"
else
  puts 'Condição falsa'
end

if (v1 < v2) || (v3 > v4)
  puts "Condição atendida por um dos casos"
else
  puts 'Condição falsa'
end

if !(v3 < v4)
  puts "Negação atendida"
else
  puts "Negação não atendida"
end