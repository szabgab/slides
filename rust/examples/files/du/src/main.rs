use std::path::Path;
use std::process::exit;

// get path on the command line
// traverse the directory tree

fn main() {
    let args: Vec<String> = std::env::args().collect();
    let path = if args.len() == 1 { Path::new(".") } else { Path::new(&args[1]) };
    if ! path.exists() {
        eprintln!("given path '{:?}' does not exist", path);
        exit(1);
    }

    let total = get_total(path);
    println!("Total: {}", total);
}

fn get_total(path: &Path) -> u64 {
    //dbg!(path);

    let mut total: u64 = 0;
    if path.is_dir() {
        for entry in path.read_dir().expect("read_dir call failed").flatten() {
            total += get_total(&entry.path());
        }
        return total
    }

    match std::fs::metadata(path) {
        Ok(meta) => {
            println!("{:?} {:?}", meta.len(), path);
            meta.len()
        },
        Err(_) => {
            eprintln!("Error in {:?}", path);
            0
        },
    }
}
