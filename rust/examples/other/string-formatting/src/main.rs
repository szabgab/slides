fn main() {
    let name = "Foo";
    let text1 = format!("Hello {}, how are you?", name);
    let text2 = format!("Hello {name}, how are you?");
    println!("{}", text1);
    println!("{}", text2);
}
