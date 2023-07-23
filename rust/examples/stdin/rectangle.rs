use std::io;
use std::io::Write;

fn main() {
    let mut length = String::new();
    let mut width = String::new();

    print!("Length: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut length)
        .expect("Faild to get input");

    let length:f32 = length
        .trim()
        .parse()
        .expect("Could not convert to f32");

    print!("Width: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut width)
        .expect("Faild to get input");

    let width:f32 = width
        .trim()
        .parse()
        .expect("Could not convert to f32");

    println!("Length: {} Width: {}, Area: {} Circumference: {}", length, width, length*width, 2.0*(length+width));
}

