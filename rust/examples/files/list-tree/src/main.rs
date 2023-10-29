use std::env;
use std::path::Path;
use std::process::exit;
use std::fs;

fn main() {
    let path = get_path();

    let tree = list_dir(Path::new(&path));
}

fn get_path() -> String {
    let args: Vec<String> = env::args().collect();

    if args.len() > 2 {
        println!("More than enough command line parameters");
        exit(1);
    }

    if args.len() == 2 {
        println!("{}", args[1]);
        return args[1].to_string();
    }

    return ".".to_string();
}


fn list_dir(path: &Path) -> Vec<String> {
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
