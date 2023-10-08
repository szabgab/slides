use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{:?}", counter);
    println!("{:?}", counter.keys());

    for (name, value) in counter.iter() {
        println!("{} : {}", name, value);
    }
    println!();

    for (name, value) in counter {
        println!("{} : {}", name, value);
    }
}
