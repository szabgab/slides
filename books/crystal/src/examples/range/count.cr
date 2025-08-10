res = (1..10).count { |ix| sprintf("%b", ix) == sprintf("%b", ix).reverse }
puts res

# puts (1..10).map{|ix| sprintf("%b", ix) ==  sprintf("%b", ix).reverse; sprintf("%b", ix) }
