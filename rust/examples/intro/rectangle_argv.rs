use std::env;
use std::process::exit;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() != 3 {
        println!("Usage {} length width", args[0]);
        exit(1);
    }
    let width: i32  = args[1].trim().parse().expect("Wanted a number");
    let height: i32 = args[2].trim().parse().expect("Wanted a number");
    let area: i32 = width * height;
    let circumference = 2 * (width + height);
    println!("area: {}", area);
    println!("circumference: {}", circumference);
}
