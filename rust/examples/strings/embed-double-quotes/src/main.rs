fn main() {
    let name = "Foo".to_string();

    println!("Hello {name}, how are you?");
    println!("Hello '{name}', how are you?");
    println!("Hello \"{name}\", how are you?");
    println!(r#"Hello "{name}", how are you?"#);
}
