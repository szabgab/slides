use std::collections::HashMap;

fn main() {
    let mut grades = HashMap::new();

    grades.insert(String::from("Joe"), 70);
    grades.insert(String::from("Jane"), 80);

    let name = String::from("Joe");
    let score = grades.get(&name);
    println!("{:?}", score);

    let score = grades[&name];
    println!("{}", score);

    let score = grades.get(&name).copied().unwrap_or(0);
    println!("{}", score);

    let name = String::from("George");
    let score = grades.get(&name).copied().unwrap_or(0);
    println!("{}", score);
}
