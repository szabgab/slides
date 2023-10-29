use std::process::exit;
use std::env;

fn main() {
    println!("to stdout");
    eprintln!("to stderr");

    let mut exit_code = 0;
    let args: Vec<String> = env::args().collect();
    if args.len() == 2 {
        exit_code = args[1].parse().unwrap();
    }
    exit(exit_code);
}
