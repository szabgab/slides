use std::io;
use std::io::Write;

fn main() {
    divide();
    divide();
    divide();
}


fn divide() {
    let a = 100;
    let b = get_number();
    let x = a / b;
    println!("{x}");
}

fn get_number() -> i32 {
    let mut number = String::new();

    print!("Please type in a number: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut number)
        .expect("Faild to get input");

    let number:i32 = number
        .trim()
        .parse()
        .expect("Could not convert to i32");

    number
}

