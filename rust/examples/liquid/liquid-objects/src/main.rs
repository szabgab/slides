fn main() {
    let template = "
        {{animal.name}}
        {{animal.height}}
    ";

    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(template).unwrap();

    let globals = liquid::object!({
        "animal": {
            "name": "elephant",
            "height": 320,
        }
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
