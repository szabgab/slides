fn main() {
    let text = String::from("mouse cat   oliphant");
    println!("{text}");
    let parts = text.split(' ');
    //let parts = text.split_whitespace();
    println!("{:?}", parts);
    for part in parts {
        println!("{}", part);
    }
    //println!("{}", parts[0]); // cannot index into a value of type `SplitWhitespace<'_>`

    //let parts: Vec<&str> = parts.collect();
    //println!("{:?}", parts);
}
