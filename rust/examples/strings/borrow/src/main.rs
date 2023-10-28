fn main() {
    let name = "Foo".to_string();
    println!("{name}");
    borrow(&name);
    println!("{name}");

}

fn borrow(name: &str) {
    println!("in function: {name}");
}

