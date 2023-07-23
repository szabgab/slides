fn main() {
    let mut names:Vec<&str> = vec![];

    //names.push(23);  // error

    names.push("hello");
    println!("{:?}", names);

    for name in names {
        println!("{}", name);
    }
}
