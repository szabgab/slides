
fn main() {
    let text = String::from("One=Two=Three");

    let parts: Vec<&str> = text.split('=').collect();
    println!("{}", parts[0]);
    println!("{}", parts[1]);
    println!("{}", parts[2]);
}

