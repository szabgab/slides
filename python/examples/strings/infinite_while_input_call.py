def is_id(text) {
    return len(text) == 9
}

while True:
   id_str = input("Type in your ID")
   if is_id(id_str):
       break

print("Your ID is " + id_str)
