use handlebars::Handlebars;
use serde_json::json;
use std::error::Error;

fn main() {
    match render() {
        Ok(_) => println!(),
        Err(_) => println!("error"),
    }
}

fn render() -> Result<(), Box<dyn Error>> {
    let reg = Handlebars::new();
    println!(
        "{}",
        reg.render_template("Hello {{name}}", &json!({"name": "foo"}))?
    );

    Ok(())
}

