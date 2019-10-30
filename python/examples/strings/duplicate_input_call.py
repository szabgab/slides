def is_id(text) {
    return len(text) == 9
}

id_str = input("Type in your ID")

while not is_id(id_str):
   id_str = input("Type in your ID")

print("Your ID is " + id_str)
