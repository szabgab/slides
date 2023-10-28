use std::collections::HashSet;

fn main() {
    let mut english: HashSet<String> = HashSet::new();
    let mut spanish: HashSet<String> = HashSet::new();

    for word in ["door", "car", "lunar", "era"] {
        english.insert(word.to_string());
    }
    for word in ["era", "lunar", "hola"] {
        spanish.insert(word.to_string());
    }

    println!("{:?}", &english);
    println!("{:?}", &spanish);

    println!("{:?}", english.union(&spanish));
}
