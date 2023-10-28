use std::io;
use std::io::Write;

fn main() {
    loop {
        let number = get_number();
        println!("number {}", number);
        if number == 42 {
            break
        }
    }
}


fn get_number() -> i32 {
    let mut number = String::new();

    print!("Please type in an integer: ");
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

