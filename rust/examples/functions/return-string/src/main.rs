fn main() {
    let name = get_name();
    println!("{}", name);
}

fn get_name() -> String {
    let fname = "Foo";
    let lname = "Bar";
    let name = format!("{} {}", fname, lname);
    println!("{}", name);
    name
}
