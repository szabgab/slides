use std::io;
use std::io::Write;

fn main() {
    let length = get_number("Length");
    let width = get_number("Width");

    println!("Length: {} Width: {}, Area: {} Circumference: {}", length, width, length*width, 2.0*(length+width));
}

fn get_number(name: &str) -> f32 {
    let mut number = String::new();
    print!("{}: ", name);
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut number)
        .expect("Faild to get input");

    let number:f32 = number
        .trim()
        .parse()
        .expect("Could not convert to i32");
    number
}

