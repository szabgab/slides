fn main() {
    let mut names = vec!["abc"];
    names.push("def");
    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
}
