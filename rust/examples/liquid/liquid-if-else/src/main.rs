fn main() {
    let template = "
        {% if at_home %}
           {{name}} is at home
        {% else %}
           {{name}} is NOT at home
        {% endif %}
    ";

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    // 1st
    let globals = liquid::object!({
        "name": "Foo Bar",
        "at_home": true,
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);

    // 2nd
    let globals = liquid::object!({
        "name": "Peti Bar",
        "at_home": false,
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
