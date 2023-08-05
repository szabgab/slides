use std::collections::HashMap;

fn main() {
    let text = String::from("apple   banana");
    println!("The original '{text}'");
    let mut data = HashMap::new();

    //let parts = text.split(" ");
    let parts = text.split_whitespace(); // return an iterator
    //println!("{:?}", parts);
    //for part in parts {
    //    println!("'{}'", part);
    //}
    //
    let parts: Vec<&str> = parts.collect(); // collect the items from an iterator to be a vector
    println!("parts: {:?}", parts);
    println!("First element '{}'", parts[0]);

    for part in parts {
        data.insert(part, part);
    }
    println!("The Hash: {:?}", data);

}
