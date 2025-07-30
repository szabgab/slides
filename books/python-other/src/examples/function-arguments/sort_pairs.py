def sort_pairs(how, **kwargs):
    if how == 'keys':
        sort_function = lambda s : s[0];
    elif how == 'values':
        sort_function = lambda s : s[1];
    else:
        raise Exception("Invalid sort function")
    return sorted(kwargs.items(), key=sort_function)



k = sort_pairs( 'keys', foo = 23, bar = 47)
print(k)
v = sort_pairs( 'values', foo = 23, bar = 47)
print(v)
