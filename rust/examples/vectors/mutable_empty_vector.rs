fn main() {
    let mut names = vec![];
    names.push(23);
    // names.push("hello"); // error
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
}

