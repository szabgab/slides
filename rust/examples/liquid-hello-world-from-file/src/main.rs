fn main() {
    let filename = String::from("template.txt");
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse_file(filename)
        .unwrap();

    let name = String::from("Liquid");
    let globals = liquid::object!({
        "name": name
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}
