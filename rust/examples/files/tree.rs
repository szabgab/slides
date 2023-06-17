use std::env;
use std::path::Path;
use std::process::exit;
use std::fs;

fn main() {
    let path = get_path();

    list_dir(Path::new(&path));
}

fn get_path() -> String {
    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
        println!("More than enough command line parameters");
        exit(1);
    }

    let mut path = ".";
    if args.len() == 2 {
        println!("{}", args[1]);
        path = &args[1];
    }

    return path.to_string();
}


fn list_dir(path: &Path) {
    for entry in path.read_dir().expect("read_dir call failed") {
        if let Ok(entry) = entry {
            println!("{:?}", entry.path());
            let metadata = fs::metadata(entry.path());
            let file_type = metadata.expect("Could not access file").file_type();
            if file_type.is_dir() {
                list_dir(&entry.path());
            }
        }
    }
}
