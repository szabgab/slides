use std::io;
use std::io::Write;

fn main() {
    let mut count = 0;
    while count < 10 {
        let number = get_number();
        count += number;
        println!("count {}", count);
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

