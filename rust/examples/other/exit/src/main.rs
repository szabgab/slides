use std::process;

fn main() {
    let early_exit = false;

    if early_exit {
        println!("Early exit");
        process::exit(3);
    }
    println!("Still running");
}
