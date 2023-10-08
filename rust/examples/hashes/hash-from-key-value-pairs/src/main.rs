use std::collections::HashMap;

fn main() {
    let input:Vec<String> = vec![
        String::from("Monday=1"),
        String::from("Tuesday=2"),
    ];

    let mut data = HashMap::new();
    for entry in input {
        let parts = mysplit(&entry);

        data.insert(parts[0].to_string(), parts[1].to_string());
    }
    println!("{:?}", data);
}

fn mysplit(entry: &str) -> Vec<&str> {
    let parts = entry.split('=');
    let parts: Vec<&str> = parts.collect();
    parts
}


