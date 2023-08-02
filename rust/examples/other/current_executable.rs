use std::env;

fn main() {
    println!("{}", env::current_exe().unwrap().display());

    match env::current_exe() {
        Ok(exe_path) => println!("Path: {}", exe_path.display()),
        Err(err) => println!("Failed to get current exe path: {err}"),
    };
}
