use std::env;
use std::path::Path;
use std::process::exit;


fn main() {
    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
        println!("More than enough command line parameters");
        exit(1);
    }

    let mut path = Path::new(".");
    if args.len() == 2 {
        println!("{}", args[1]);
        path = Path::new(&args[1]);
    }

    for entry in path.read_dir().expect("read_dir call failed").flatten() {
        println!("{:?}", entry.path());
    }
}
