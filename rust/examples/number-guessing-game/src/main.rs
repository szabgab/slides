fn main() {
    let guess = get_guess();
    println!("{}", guess);
}

fn get_guess() -> i32 {
    let mut input = String::new();
    std::io::stdin()
        .read_line(&mut input)
        .expect("Error in reading from STDIN");
    println!("{}", input);
    return 23;
}
