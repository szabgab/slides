fn main() {
    let names = ["name.txt", "other"];
    for name in names {
        print!("name: '{}'", name);
        if name.ends_with(".txt") {
            print!(" ends with .txt");
        }
        println!();
    }
}
