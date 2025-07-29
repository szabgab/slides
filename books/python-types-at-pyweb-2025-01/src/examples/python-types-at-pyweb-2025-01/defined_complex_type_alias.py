ReturnType = dict[str, int]
result: ReturnType = {
        "blue": 1,
        "green": 0,
}
#result: ReturnType = {
#        "blue": "ok",
#        "green": 0,
#}

# ------------------------------------------

UnionReturnType = dict[str, str | int]
ret: UnionReturnType = {
        "blue": "ok",
        "green": 0,
}


