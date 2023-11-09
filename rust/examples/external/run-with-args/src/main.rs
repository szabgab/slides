use std::process::Command;

fn main() {
    // ls -l -a -s
    let result = Command::new("ls")
        .args(["-l", "-a", "-s"])
        .output()
        .expect("ls command failed to start");

    println!("stdout:\n{}", std::str::from_utf8(&result.stdout).unwrap());
    println!("stderr:\n{}", std::str::from_utf8(&result.stderr).unwrap());
    println!("{}", result.status);
}
