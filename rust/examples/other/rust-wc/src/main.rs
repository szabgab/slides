use std::env;

fn main() {
    // get the path from the command line
    // if it is a file work on it
    // if it is a folder ...
    // get command line parameters

    let files: Vec<String> = env::args().collect();
    for file in &files[1..files.len()] {
        dbg!(file);
    }
}
