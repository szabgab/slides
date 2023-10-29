use std::fs::File;
use std::io::Read;
use std::io::Write;

fn main() {
    let filename = "count.txt";
    let mut content = String::new();

    match File::open(filename) {
        Ok(mut file) => {
            file.read_to_string(&mut content).unwrap();
        },
        Err(_) => {
            content = "0".to_string();
        },
    }
    let mut counter: i32 = content.trim().parse().expect("Wanted a number");
    counter += 1;
    println!("{}", counter);

    let mut file = File::create(filename).unwrap();
    writeln!(&mut file, "{}", counter).unwrap();
}
