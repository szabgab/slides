use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "rust.json";
    match File::open(filename) {
        Ok(file) => {
            let reader = BufReader::new(file);
            for (index, line) in reader.lines().enumerate() {
                let line = line.unwrap();
                println!("{}. {}", index + 1, line);
            }
        },
        Err(error) => {
            println!("Error opening file {}: {}", filename, error);
        },
    }
}
