use std::fs::File;
use std::io::Read;

fn main() {
    let filepath = "planets.csv";
    println!("Hello, world!");
    read_file(filepath);
}

fn read_file(filepath: &str) {
    match File::open(filepath.to_string()) {
        Ok(mut file) => {
            let mut content = String::new();

            file.read_to_string(&mut content).unwrap();

            println!("{}", content);
            //return content;
        },
        Err(error) => {
            println!("Error opening file {}: {}", filepath, error);
        },
    }
}
