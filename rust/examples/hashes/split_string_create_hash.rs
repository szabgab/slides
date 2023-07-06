use std::collections::HashMap;

fn main() {
    let text = String::from("apple   banana");
    println!("{text}");
    let mut data = HashMap::new();

    //let parts = text.split(" ");
    let parts = text.split_whitespace(); // return an iterator
    //println!("{:?}", parts);
    //for part in parts {
    //    println!("'{}'", part);
    //}
    //
    let parts: Vec<&str> = parts.collect();
    println!("{:?}", parts);
    println!("{}", parts[0]);

    for part in parts {
        data.insert(part, part);
    }
    println!("{:?}", data);

}
