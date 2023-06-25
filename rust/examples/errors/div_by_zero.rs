use std::io;
use std::io::Write;

fn main() {
    loop {
        let num = get_number();
        if num == 0 {
            panic!("Cannot divide by 0");
        }
        divide_by(num);
    }
}


fn divide_by(num: i32) {
    let a = 100;
    let x = a / num;
    println!("{a} / {num} = {x}");
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

