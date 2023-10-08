use handlebars::Handlebars;
use serde_json::json;
use std::error::Error;
use std::fs::File;
use std::io::Write;
use std::io::Read;


fn main() {
    let filename = "hello.html";
    let template = "template.html";
    match render_without_register(template, filename) {
        Ok(_) => println!(),
        Err(_) => println!("error"),
    }
}

fn render_without_register(template_file: &str, filename: &str) -> Result<(), Box<dyn Error>> {
    let mut template = String::new();
    match File::open(template_file) {
        Ok(mut file) => {
            file.read_to_string(&mut template).unwrap();
        },
        Err(error) => {
            println!("Error opening file {}: {}", template_file, error);
        },
    }

    let reg = Handlebars::new();
    let fruits = ["apple", "banana", "peach"];
    let html = reg.render_template(&template, &json!({"fruits": fruits}))?;
    let mut file = File::create(filename).unwrap();
    writeln!(&mut file, "{}", html).unwrap();

    Ok(())
}

