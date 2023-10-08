use std::fs::File;
use std::io::Read;

pub type Partials = liquid::partials::EagerCompiler<liquid::partials::InMemorySource>;

fn main() {
    let mut partials = Partials::empty();
    let filename ="templates/incl/header.txt";
    partials.add(filename, read_file(filename));

    let template = liquid::ParserBuilder::with_stdlib()
        .partials(partials)
        .build()
        .unwrap()
        .parse_file("templates/page.txt")
        .unwrap();

    let globals = liquid::object!({
        "title": "Liquid",
        "name": "Foo Bar",
        "value": "some value",
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}


fn read_file(template_file: &str) -> String {
    let mut template = String::new();
    match File::open(template_file) {
        Ok(mut file) => {
            file.read_to_string(&mut template).unwrap();
        },
        Err(error) => {
            println!("Error opening file {}: {}", template_file, error);
        },
    }
    template
}

