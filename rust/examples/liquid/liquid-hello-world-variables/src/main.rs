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

    // 2nd
    let name = "Liquid - 2";
    let globals = liquid::object!({
        "name": name
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);

    // 3rd
    let name = String::from("Liquid - 3");
    let globals = liquid::object!({
        "name": name
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
