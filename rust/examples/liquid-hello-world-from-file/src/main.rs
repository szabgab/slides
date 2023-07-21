use std::fs::File;
use std::io::Read;

fn main() {
    let template = read_template("template.txt");
    let template = liquid::ParserBuilder::with_stdlib()
        .build()
        .unwrap()
        .parse(&template).unwrap();

    let name = String::from("Liquid");
    let globals = liquid::object!({
        "name": name
    });
    let output = template.render(&globals).unwrap();
    println!("{}", output);
}


fn read_template(template_file: &str) -> String {
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

