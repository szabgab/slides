use std::collections::HashMap;

fn main() {
    let mut counter = HashMap::new();
    *counter.entry("apple").or_insert(0) += 1;
    println!("{:#?}", counter);

    *counter.entry("banana").or_insert(0) += 1;
    println!("{:#?}", counter);

    *counter.entry("apple").or_insert(0) += 1;
    println!("{:#?}", counter);
}
