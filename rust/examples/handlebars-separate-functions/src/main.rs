use handlebars::Handlebars;
use serde_json::json;
use std::error::Error;

fn main() {
    match render_without_register() {
        Ok(_) => println!(""),
        Err(_) => println!("error"),
    }

    match render_register_template_using_name() {
        Ok(_) => println!(""),
        Err(_) => println!("error"),
    }
}

fn render_without_register() -> Result<(), Box<dyn Error>> {
    let reg = Handlebars::new();
    println!(
        "{}",
        reg.render_template("Hello {{name}}", &json!({"name": "foo"}))?
    );

    Ok(())
}

fn render_register_template_using_name() -> Result<(), Box<dyn Error>> {
    let mut reg = Handlebars::new();
    reg.register_template_string("tpl_1", "Good afternoon, {{name}}")?;
    println!("{}", reg.render("tpl_1", &json!({"name": "foo"}))?);
    println!("{}", reg.render("tpl_1", &json!({"name": "bar"}))?);

    Ok(())
}

