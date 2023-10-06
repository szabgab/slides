use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{:?}", counter.contains_key("zz"));
    println!("{:?}", counter.contains_key("foo"));
}
