fn main() {
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse("Welcome to {{name}}").unwrap();

    let globals = liquid::object!({
        "name": "Liquid"
    });
    let output = template.render(&globals).unwrap();

    println!("{}", output);
}
