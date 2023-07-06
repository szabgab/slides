use std::collections::HashMap;

fn main() {
    let mut counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{:?}", counter);
    println!("{:?}", counter.keys());
    let was = counter.remove("foo");
    println!("{:?}", was);
    println!("{:?}", counter);
    println!("{:?}", counter.keys());

}
