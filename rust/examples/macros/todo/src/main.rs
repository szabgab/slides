fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 2 {
        println!("Usage: {} name", &args[0]);
        std::process::exit(1);
    }
    let val = &args[1];
    if val == "foo" {
        println!("ok");
    } else {
        todo!();
        //unimplemented!();
    }
}
