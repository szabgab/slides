use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{}", counter["foo"]);
    println!("{:?}", counter.get("foo"));

    // println!("{}", counter["zz"]); // panic
    println!("{:?}", counter.get("zz")); // None
}
