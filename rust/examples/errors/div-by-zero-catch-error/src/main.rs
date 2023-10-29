use std::io;
use std::io::Write;

fn main() {
    loop {
        let dividend = 100;
        let divisor = get_number();
        match divide_by(dividend, divisor) {
            Ok(val) => println!("{dividend} / {divisor} = {val}"),
            Err(error) => println!("Error {:?}", error),
        };
    }
}


fn divide_by(dividend: i32, divisor: i32) -> Result<i32, &'static str> {
    if divisor == 0 {
        return Err("Cannot divide by 0");
    }
    let res = dividend / divisor;
    Ok(res)
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

