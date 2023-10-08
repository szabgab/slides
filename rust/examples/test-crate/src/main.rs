//use std::process::Command;
use std::env;

fn main() {
    let folder = get_url();
    println!("{}", folder);
    // get a repo url on the command line
    //
    // create a temporary directory
    // clone the repo there
    // run the tests in the docker
    // capture the output


    //let result = Command::new("docker"
    //        .arg("run --rm --workdir /opt -v$(pwd):/opt -it --user tester rust-test cargo test")
    //        .output()
    //        .expect("failed to execute process");
    //println!("{}", std::str::from_utf8(&result.stdout).unwrap());
    //println!("{}", std::str::from_utf8(&result.stderr).unwrap());
    //println!("{}", result.status);
}

fn get_url() -> String {
    let args: Vec<String> = env::args().collect();
    if args.len() != 2 {
        std::process::exit(1);
    }
    args[1].clone()
}
