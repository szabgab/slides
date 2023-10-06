use std::collections::HashMap;

fn main() {
    let mut counter = HashMap::new();
    println!("{}", counter.len());
    println!("{:?}", counter);

    counter.insert("foo", 1);
    counter.insert("bar", 2);
    println!("{:?}", counter.len());
    println!("{:?}", counter);
}
