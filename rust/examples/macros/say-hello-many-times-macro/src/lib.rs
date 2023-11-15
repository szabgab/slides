extern crate proc_macro;
use proc_macro::TokenStream;


#[proc_macro]
pub fn say_hello(input: TokenStream) -> TokenStream {
    println!("Input: {}", input);
    let value = input.to_string();
    println!("Value: {}", value);

    let values = value.split(',').map(|val| val.trim()).collect::<Vec<&str>>();
    let mut code = "".to_string();
    for val in values {
        code += format!(r#"println!("Hello '{val}'");"#).as_str();
    }

    code.parse().unwrap()

}

