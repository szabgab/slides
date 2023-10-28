use std::collections::HashSet;

fn main() {
    let mut english: HashSet<String> = HashSet::new();
    println!("{:?}", &english);

    english.insert("chair".to_string());
    println!("{:?}", &english);

    english.insert("table".to_string());
    println!("{:?}", &english);

    english.insert("chair".to_string());
    println!("{:?}", &english);

    println!("{}", english.contains("chair"));
    println!("{}", english.contains("door"));
    println!("{}", english.len());

    for word in &english {
        println!("{}", word);
    }

    english.remove("chair");
    println!("{:?}", &english);
}
