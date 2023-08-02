use std::process::Command;

fn main() {
    let result = Command::new("./all")
            .arg("3")
            .output()
            .expect("failed to execute process");
    println!("{}", std::str::from_utf8(&result.stdout).unwrap());
    println!("{}", std::str::from_utf8(&result.stderr).unwrap());
    println!("{}", result.status);
}
