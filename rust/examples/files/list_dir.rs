use std::path::Path;

fn main() {

    let path = Path::new(".");
    for entry in path.read_dir().expect("read_dir call failed") {
        if let Ok(entry) = entry {
            println!("{:?}", entry.path());
        }
    }
}
