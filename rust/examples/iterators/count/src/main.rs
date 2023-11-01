fn main() {
    let numbers = [3, 4, 5];
    println!("{}", numbers.len());
    println!("{}", numbers.iter().count());

    // An iterator
    let readdir = std::path::Path::new(".").read_dir().unwrap();
    println!("{:?}", readdir);
    println!("{}", readdir.count());
}
