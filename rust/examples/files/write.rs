use std::fs::File;
use std::io::Write;


fn main() {
    let filename = "data.txt";
    let mut file = File::create(filename).unwrap();
    writeln!(&mut file, "Hello World!").unwrap();
}
