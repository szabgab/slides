use std::process::Command;

fn main() {
    let command = "ls -l -a -s";
    let parts: Vec<&str> = command.split(' ').collect();
    //println!("{:?}", parts);

    let cmd = &parts[0];
    let args = &parts[1..parts.len()];

    let result = Command::new(cmd)
        .args(args)
        .output()
        .expect("ls command failed to start");

    println!("stdout:\n{}", std::str::from_utf8(&result.stdout).unwrap());
    println!("stderr:\n{}", std::str::from_utf8(&result.stderr).unwrap());
    println!("{}", result.status);
}
