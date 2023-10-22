use std::env;

fn main() {
    let args: Vec<String> = env::args().collect();
    println!("My path is {}", args[0]);
    println!("Number of arguments is {}", args.len());

    for i in 1..args.len() {
        println!("Parameter {} is '{}'", i, args[i]);
    }
}
