fn main() {
    let template = "
        {% for color in thing.colors %}
           {{color}}
        {% endfor %}
    ";

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    let globals = liquid::object!({
        "thing": {
            "colors": ["red", "green", "blue"],
        }
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
