use std::env::current_dir;

fn main() {
    let folder = current_dir().unwrap();
    println!("{:?}", folder);
    println!("{}", folder.display());
}
