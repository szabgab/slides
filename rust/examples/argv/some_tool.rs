use std::env;
use std::process;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        eprintln!("Usage: {} FILENAME", args[0]);
        process::exit(1);
    }

    let filename = &args[1];
    println!("We are working on file '{}'", filename);

}
