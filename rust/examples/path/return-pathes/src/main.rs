use std::path::{Path, PathBuf};

fn main() {
    let pathes = get_pathes();
    println!("{:?}", pathes);
    for path in pathes {
        println!("{:?}", path);
        //println!("{}", path.display());
        //println!("{:?}", path.parent());
    }
}

fn get_pathes() -> Vec<PathBuf> {
    let mut entries = vec![];
    let path = Path::new(".");
    for entry in path.read_dir().expect("read_dir call failed").flatten() {
        entries.push(entry.path());
    }
    entries
}

