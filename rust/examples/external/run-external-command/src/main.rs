use std::process::Command;

fn main() {
    check(3);
    check(0);
}

fn check(exit_code: i32) {
    let result = Command::new("../all/target/release/all")
        .arg(format!("{exit_code}"))
        .output()
        .expect("failed to execute process");
    print!("{}", std::str::from_utf8(&result.stdout).unwrap());
    print!("{}", std::str::from_utf8(&result.stderr).unwrap());
    println!("{}", result.status);

    assert_eq!(std::str::from_utf8(&result.stdout).unwrap(), "to stdout\n");
    assert_eq!(
        std::str::from_utf8(&result.stderr).unwrap(),
        format!("to stderr. Exit code {}\n", exit_code)
    );
    if exit_code == 0 {
        assert!(result.status.success());
    }
    assert_eq!(result.status.code().unwrap(), exit_code);
    println!();
}
