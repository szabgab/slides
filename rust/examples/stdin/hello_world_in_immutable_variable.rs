fn main() {
    let text = "Hello World!";
    println!("{}", text);
    text = "Something else";  // cannot assign twice to immutable variable
    println!("{}", text);
}

