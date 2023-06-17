use std::cmp::Ordering;
use std::io;
use rand::Rng;

fn main() {
    println!("Number Guessing game");

    let secret_number = rand::thread_rng().gen_range(1..=100);

    loop {
        println!("Print input your guess");

        let mut guess = String::new();
        io::stdin()
            .read_line(&mut guess)
            .expect("Failed to read line");
        guess = guess.trim().to_string();

        if guess == "s" {
            println!("The secret number is {secret_number}");
            continue;
        }
        if guess == "x" || guess == "q" {
            println!("Quitter!");
            break;
        }

        println!("You guessed {guess}");

        let guess: u32 = match guess.parse() {
            Ok(num) => num,
            Err(err)  => {
                println!("Error: {err}");
                continue;
            }
        };

        match guess.cmp(&secret_number) {
            Ordering::Less => println!("Too small!"),
            Ordering::Greater => println!("Too big!"),
            Ordering::Equal => {
                println!("You win!");
                break;
            }
        }
    }
}
