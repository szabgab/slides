use std;
use std::io::Write;

fn main() {
    let mut name = String::new();

    print!("Please type in your name: ");
    std::io::stdout().flush().expect("Oups");
    std::io::stdin()
        .read_line(&mut name)
        .expect("Faild to get input");
    name = name.trim_end().to_string();

    println!("Hello {}, how are you?", name);
}
