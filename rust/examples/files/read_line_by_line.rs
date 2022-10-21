use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    let filename = "rust.json";
    match File::open(filename) {
        Ok(file) => {
            let reader = BufReader::new(file);
            for line in reader.lines() {
                let line = line.unwrap();
                println!("{}", line);
            }
        },
        Err(error) => {
            println!("Error opening file {}: {}", filename, error);
        },
    }
}
