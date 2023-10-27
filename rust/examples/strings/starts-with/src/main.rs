fn main() {
    let names = ["name.txt", "other", "narnia"];
    for name in names {
        print!("name: '{}'", name);
        if name.starts_with("na") {
            print!(" starts with na");
        }
        println!();
    }
}
