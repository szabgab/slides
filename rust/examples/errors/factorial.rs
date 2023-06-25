use std::io;
use std::io::Write;

fn main() {
    loop {
        let number = get_number();
        let fact = factorial(number);
        println!("{number}! is {fact}");
    }
}

fn factorial(n:i64) -> i64 {
    if n == 0 {
        return 1;
    }
    return n * factorial(n-1);
}


fn get_number() -> i64 {
    let mut number = String::new();

    print!("Please type in a number: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut number)
        .expect("Faild to get input");

    let number:i64 = number
        .trim()
        .parse()
        .expect("Could not convert to i64");

    number
}

