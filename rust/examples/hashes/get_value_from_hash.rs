use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{}", counter["foo"]);
    println!("{:?}", counter.get("foo"));

    // println!("{}", counter["zz"]); // panick
    println!("{:?}", counter.get("zz")); // None
    println!("{:?}", counter.contains_key("zz")); // false
    println!("{:?}", counter.contains_key("foo")); // true
}
