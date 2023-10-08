use handlebars::Handlebars;
use serde_json::json;
use std::error::Error;
use std::fs::File;
use std::io::Write;
use std::io::Read;
use chrono::{Utc, DateTime};


fn main() {
    let filename = "hello.html";
    let template = "template.html";
    match render_without_register(template, filename) {
        Ok(_) => println!(),
        Err(_) => println!("error"),
    }
}

fn render_without_register(template_file: &str, filename: &str) -> Result<(), Box<dyn Error>> {
    let template = read_template(template_file);

    let utc: DateTime<Utc> = Utc::now();

    let reg = Handlebars::new();
    let html = reg.render_template(&template, &json!({"utc": format!("{}", utc)}))?;
    let mut file = File::create(filename).unwrap();
    writeln!(&mut file, "{}", html).unwrap();

    Ok(())
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

