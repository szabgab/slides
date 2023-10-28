use std::io;
use std::io::Write;

fn main() {
    let mut height = String::new();

    print!("Please type in your height in cm: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut height)
        .expect("Faild to get input");

    let height:i32 = height
        .trim()
        .parse()
        .expect("Could not convert to i32");

    println!("Your height is 1 cm less than {}", height+1);
}
