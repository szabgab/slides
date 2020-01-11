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

print(json.dumps(data, sort_keys=True, indent=4, separators=(',', ': ')))

