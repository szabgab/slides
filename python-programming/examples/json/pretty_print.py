import json

data = {
    "name" : "Foo Bar",
    "grades" : [23, 47, 99, 11],
    "children" : {
        "Peti Bar" : {
            "email": "peti@bar.com",
        },
        "Jenny Bar" : {
            "phone": "12345",
        },
    }
}

print(data)
print(json.dumps(data))
print(json.dumps(data, indent=4, separators=(',', ': ')))
