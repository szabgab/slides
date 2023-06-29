use std::collections::HashMap;

fn main() {
    let mut counter = HashMap::new();
    println!("{}", counter.len());

    counter.insert("foo", 1);
    counter.insert("bar", 2);
    println!("{:?}", counter);
    println!("{:?}", counter.len());
    println!("{:?}", counter.keys());

    for name in counter.keys() {
        println!("{} : {}", name, counter[name]);
    }

    for (name, value) in counter {
        println!("{} : {}", name, value);
    }
}
