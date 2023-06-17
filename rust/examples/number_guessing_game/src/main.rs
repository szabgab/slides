use std::io;

fn main() {
    println!("Number Guessing game");
    println!("Print input your guess");

    let mut guess = String::new();
    io::stdin()
        .read_line(&mut guess)
        .expect("Failed to read line");
    println!("You guessed {guess}");
}
