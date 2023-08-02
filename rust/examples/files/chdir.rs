use std::env;

fn main() {
    let folder = env::current_dir().unwrap();
    println!("{:?}", folder);

    env::set_current_dir("/tmp").unwrap();

    let folder = env::current_dir().unwrap();
    println!("{:?}", folder);
}
