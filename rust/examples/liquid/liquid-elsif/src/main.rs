fn main() {
    let template = r#"
        {% if color == "blue" %}
            blue
        {% elsif color == "green" %}
            green
        {% else %}
            Unrecognized color
        {% endif %}
    "#;

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    // 1st
    let globals = liquid::object!({
        "color": "blue",
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);

    // 2nd
    let globals = liquid::object!({
        "color": "green",
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);

    // 3rd
    let globals = liquid::object!({
        "color": "red",
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);

}
