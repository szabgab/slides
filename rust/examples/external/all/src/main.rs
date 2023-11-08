use std::env;
use std::process::exit;

fn main() {
    let mut exit_code = 0;
    let args: Vec<String> = env::args().collect();
    if args.len() == 2 {
        exit_code = args[1].parse().unwrap();
    }

    println!("to stdout");
    eprintln!("to stderr. Exit code {}", exit_code);
    exit(exit_code);
}
