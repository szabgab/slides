use std::collections::HashMap;

fn main() {
    let fruits = ["apple", "banana", "peach", "apple"];
    let mut counter = HashMap::new();

    for fruit in fruits {
        println!("{}", fruit);
        *counter.entry(fruit).or_insert(0) += 1;
    }
    println!("{:#?}", counter);
}
