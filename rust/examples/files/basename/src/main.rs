use std::path::Path;

fn main() {
    let path = Path::new("root/subdir/folder/filename.rs");
    println!("{}", path.file_name().unwrap().to_str().unwrap());
}
