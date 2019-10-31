def is_float(input):
    try:
        num = float(input)
    except ValueError:
        return False
    return True

def is_int(input):
    try:
        num = int(input)
    except ValueError:
        return False
    return True

print( is_float("23") )      # True
print( is_float("23.2") )    # True
print( is_float("23x") )     # False
print( '-----' )             # -----
print( is_int("23") )        # True
print( is_int("23.2") )      # False
print( is_int("23x") )       # False

