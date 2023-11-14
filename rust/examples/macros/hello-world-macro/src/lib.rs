extern crate proc_macro;
use proc_macro::TokenStream;

#[proc_macro]
pub fn hello_world(_item: TokenStream) -> TokenStream {
    println!("Hello World during compilation");

    //"println!(\"Hello World that was added to the code\");".parse().unwrap()
    r#"println!("Hello World that was added to the code");"#.parse().unwrap()
}
