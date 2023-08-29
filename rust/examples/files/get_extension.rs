use std::path::Path;


fn main() {
    let path = Path::new("a/b/code.rs");
    println!("{:?}", path.extension().unwrap());
    println!("{:?}", path.extension().unwrap() == "rs");

    let path = Path::new("a/b/code");
    match path.extension() {
        Some(value) => println!("{:?}", value),
        None => println!("Has no extension"),
    };
}
