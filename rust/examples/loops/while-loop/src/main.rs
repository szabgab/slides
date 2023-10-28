use std::io;
use std::io::Write;

fn main() {
    let mut total = 0;
    while total < 10 {
        let number = get_number();
        total += number;
        println!("total {}", total);
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

