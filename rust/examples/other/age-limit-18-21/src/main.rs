use std::io;
use std::io::Write;

fn main() {

    let mut age = String::new();

    print!("How old are you? ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut age)
        .expect("Faild to get input");

    let age: f32 = age.trim().parse().unwrap_or_else(|_| panic!("Could not convert '{age}' to floating point number"));
    if age < 18.0 {
        println!("You are under 18. You cannot legally drink alcohol!");
    } else if age >= 21.0 {
        println!("Congratulations, you can legally drink alcohol! Even in the USA.");
    } else {
        println!("You can drink alcohol, unless you are in the USA.");
    }
}
