fruits_vector = c("Apple", "Banana", "Apple", "Apple", "Peach", "Banana")
fruits_factor  = as.factor(fruits_vector)

fruits_vector   # [1] "Apple"  "Banana" "Apple"  "Apple"  "Peach"  "Banana"

fruits_factor   # [1] Apple  Banana Apple  Apple  Peach  Banana
                # Levels: Apple Banana Peach

class(fruits_vector)  # "character"
class(fruits_factor)  # "factor"

length(fruits_vector) # 6
length(fruits_factor) # 6

levels(fruits_vector) # NULL
levels(fruits_factor) # "Apple"  "Banana" "Peach"

fruits_vector["Apple"] # NA
fruits_factor["Apple"] # [1] <NA>
                       # Levels: Apple Banana Peach

