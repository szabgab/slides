fn main() {
    let args: Vec<String> = std::env::args().collect();
    if args.len() < 2 || args.len() > 3 {
        eprintln!("Usage: {} ROOT [PATH]", args[0]);
        std::process::exit(1);
    }
    let root = &args[1];
    let page = get_path(&args);
    println!("root: {}", root);
    println!("page: {:?}", page);
}

fn get_path(args: &Vec<String>) -> std::path::PathBuf {
    if args.len() == 3 {
        return std::path::PathBuf::from(&args[2]);
    }
    let pb = std::path::PathBuf::from(&args[1]);
    pb.join("pages")
}
