use ansi_term::Colour::{Blue, Green, Red};

fn main() {
    println!("Hello, world!");
    println!("{}", Blue.bold().paint("blue"));
    println!("{}", Green.dimmed().paint("green"));

    println!("Hello {} sky and {} grass!", Blue.bold().paint("blue"), Green.bold().paint("green"));
    println!("{}", Red.bold().paint("red"));
}
