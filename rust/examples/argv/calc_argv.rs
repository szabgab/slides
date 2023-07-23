fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() != 4 {
        eprintln!("Usage {} a operator b", args[0]);
        eprintln!("Received {} parameters", args.len());
        std::process::exit(1);
    }
    let var_a: f64  = args[1].trim().parse().expect("Wanted a number");
    let op: &String = &args[2];
    let var_b: f64 = args[3].trim().parse().expect("Wanted a number");
    let res: f64;
    if op == "+" {
        res = var_a + var_b;
    } else if op == "-" {
        res = var_a - var_b;
    } else if op == "*" {
        res = var_a * var_b;
    } else if op == "/" {
        res = var_a / var_b;
    } else {
        eprintln!("Unrecognized operator '{op}'");
        std::process::exit(1);
    }

    println!("{var_a} {op} {var_b} = {res}");
}
