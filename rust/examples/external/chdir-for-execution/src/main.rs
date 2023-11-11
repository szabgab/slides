use std::process::Command;

fn main() {
    let result = Command::new("pwd")
        .output()
        .expect("pwd command failed to start");
    print!("{}", std::str::from_utf8(&result.stdout).unwrap());

    let result = Command::new("pwd")
        .current_dir("src")
        .output()
        .expect("pwd command failed to start");
    print!("{}", std::str::from_utf8(&result.stdout).unwrap());

    let result = Command::new("pwd")
        .current_dir("/etc/")
        .output()
        .expect("pwd command failed to start");
    print!("{}", std::str::from_utf8(&result.stdout).unwrap());

    println!("{}", std::env::current_dir().unwrap().display());
}
