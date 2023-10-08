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
    let mut reg = Handlebars::new();
    reg.register_template_string("tpl_1", "Good afternoon, {{name}}")?;

    println!("{}", reg.render("tpl_1", &json!({"name": "foo"}))?);
    println!("{}", reg.render("tpl_1", &json!({"name": "bar"}))?);

    Ok(())
}

