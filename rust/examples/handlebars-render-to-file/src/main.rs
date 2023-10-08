use handlebars::Handlebars;
use serde_json::json;
use std::error::Error;
use std::fs::File;
use std::io::Write;

fn main() {
    match render_without_register("hello.html") {
        Ok(_) => println!(),
        Err(_) => println!("error"),
    }
}

fn render_without_register(filename: &str) -> Result<(), Box<dyn Error>> {
    let reg = Handlebars::new();
    let html = reg.render_template("Hello {{name}}", &json!({"name": "foo"}))?;
    let mut file = File::create(filename).unwrap();
    writeln!(&mut file, "{}", html).unwrap();

    Ok(())
}

