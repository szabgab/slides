use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{:?}", counter);
    println!("{:?}", counter.keys());

    for name in counter.keys() {
        println!("{} : {}", name, counter[name]);
    }
}
