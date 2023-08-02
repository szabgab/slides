use std::env;

fn main() {
    let folder = env::temp_dir();
    println!("{:?}", folder);
}
