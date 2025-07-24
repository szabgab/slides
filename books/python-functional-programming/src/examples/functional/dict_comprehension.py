people = {
    'Foo':       123,
    'Bar':       456,
    'SnowWhite': 7,
}

doubles = { k:v*2 for (k, v) in people.items() }
print(doubles)  # {'Foo': 246, 'Bar': 912, 'SnowWhite': 14}

