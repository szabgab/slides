fn main() {
    let text = "The black cat";
    println!("{text}");
    println!("{:?}", text.chars());

    for c in text.chars() {
        println!("{c}");
    }
}
