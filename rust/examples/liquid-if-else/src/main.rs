fn main() {
    let template = "
        {{thing.name}}

        {% for color in thing.colors %}
           {{color}}
        {% endfor %}

        {% for animal in thing.animals %}
            {% if animal.real %}
                A real {{animal.name}}
            {% else %}
                A fake {{animal.name}}
            {% endif %}
        {% endfor %}
    ";

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    let globals = liquid::object!({
        "thing": {
            "name": "Foo Bar",
            "colors": ["red", "green", "blue"],
            "animals": [
                {
                    "name": "mouse",
                    "real": true,
                },
                {
                    "name": "snake",
                    "real": true,
                },
                {
                    "name": "oliphant",
                    "real": false,
                },
            ],
        }
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
