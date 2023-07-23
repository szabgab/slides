use std::io;
use std::io::Write;

fn main() {
    let mut var_a = String::new();
    let mut op = String::new();
    let mut var_b = String::new();

    print!("a: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut var_a)
        .expect("Faild to get input");

    let var_a:f64 = var_a
        .trim()
        .parse()
        .expect("Could not convert to f64");

    print!("op: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut op)
        .expect("Faild to get input");
    op = op.trim().to_string();

    print!("b: ");
    io::stdout().flush().expect("Oups");
    io::stdin()
        .read_line(&mut var_b)
        .expect("Faild to get input");

    let var_b:f64 = var_b
        .trim()
        .parse()
        .expect("Could not convert to f64");

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
