macro_rules! create_counter {
    ($( $name: expr ),*) => {
        std::collections::HashMap::from([
            $(
                ($name, 0),
            )*
        ])
    };
}

fn main() {
    let mut counter = create_counter!("cat", "dog");

    // This basically generates code like this:
    // let mut counter = std::collections::HashMap::from([
    //     ("cat", 0),
    //     ("dog", 0),
    // ]);

    println!("{:?}", counter);
    *counter.entry("dog").or_insert(0) += 1;
    println!("{:?}", counter);
}
