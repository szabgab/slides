use std::collections::HashMap;

fn main() {

    let mut pairs: Vec<(String, i32)> = vec![
            ("snake".to_string(), 1),
            ("dog".to_string(),   2),
        ];
    let cat = ("cat".to_string(), 3);
    pairs.push(cat);
    println!("vector of pairs: {:?}", pairs);

    let counter: HashMap<String, i32> = HashMap::from_iter(pairs);
    println!("hash: {:?}", counter);
    println!("dog: {:?}", counter["dog"]);
}
