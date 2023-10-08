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

    //let colors: [&str; 3] = ["red", "green", "blue"];
    let colors = vec!["red", "green", "blue"];

    let globals = liquid::object!({
        "thing": {
            "colors": colors,
        }
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
