use std::io;

fn main() {
    let mut name = String::new();

    println!("Please type in your name:");
    io::stdin()
        .read_line(&mut name)
        .expect("Faild to get input");

    println!("Hello {}, how are you?", name);
}
