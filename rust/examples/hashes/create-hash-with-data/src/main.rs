use std::collections::HashMap;

fn main() {
    let counter = HashMap::from([
        ("foo", 1),
        ("bar", 2),
    ]);
    println!("{:?}", counter);
    println!("{:?}", counter.keys());

    // counter.insert("other", 3); // cannot borrow `counter` as mutable, as it is not declared as mutable
}
