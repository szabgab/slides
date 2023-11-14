extern crate proc_macro;
use proc_macro::TokenStream;

#[proc_macro]
pub fn get_random(item: TokenStream) -> TokenStream {
    match item.to_string().as_str() {
        "u16" => {
            let x = rand::random::<u16>();
            format!("{:?}", x).parse().unwrap()
        },
        "i32" => {
            let x = rand::random::<i32>();
            format!("{:?}", x).parse().unwrap()
        },
        _ => panic!("Unsupported type '{}'", item),
    }
}
