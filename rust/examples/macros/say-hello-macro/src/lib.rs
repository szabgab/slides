extern crate proc_macro;
use proc_macro::TokenStream;


#[proc_macro]
pub fn say_hello(input: TokenStream) -> TokenStream {
    println!("Input: {}", input);

    let value = input.to_string();
    println!("Value: {}", value);

    let code = format!(r#"println!("Hello {value}");"#);
    code.parse().unwrap()
}

