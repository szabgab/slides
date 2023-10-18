fn main() {
    let mut names = vec![];
    println!("{:?}", names);

    names.push(23);

    // names.push("hello"); // error[E0308]: mismatched types - expected integer, found `&str`
    // names.push(3.14);    // error[E0308]: mismatched types - expected integer, found floating-point number
    names.push(19);

    println!("{:?}", names);
    for name in names {
        println!("{}", name);
    }
}

