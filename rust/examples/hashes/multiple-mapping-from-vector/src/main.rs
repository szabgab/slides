use std::collections::HashMap;


#[derive(Debug)]
#[allow(dead_code)]
struct Something {
    key1: String,
    key2: String,
}

fn main() {
    let things: Vec<Something> = vec![
        Something { key1: "one".to_string(), key2: "two".to_string() },
        Something { key1: "uno".to_string(), key2: "dos".to_string() },
    ];
    dbg!(&things);

    let mut mapping_from_key1: HashMap<String, &Something> = HashMap::new();
    let mut mapping_from_key2: HashMap<String, &Something> = HashMap::new();
    for thing in &things {
        mapping_from_key1.insert(thing.key1.clone(), thing);
        mapping_from_key2.insert(thing.key2.clone(), thing);
    }

    dbg!(&mapping_from_key1);
    dbg!(&mapping_from_key2);
}
