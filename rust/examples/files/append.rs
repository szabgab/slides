use std::fs::File;
use std::io::Write;

fn main() {
    let filename = "data.txt";
    let mut fh = match File::options().append(true).open(filename) {
        Ok(fh) => fh,
        Err(_) => {
            File::create(filename).unwrap()
        }
    };
    writeln!(&mut fh, "Hello").unwrap();
}
