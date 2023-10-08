use std::collections::HashMap;

fn main() {
    let mut grades = HashMap::new();

    grades.insert(String::from("Joe"), 70);  // create
    println!("{}", grades["Joe"]);

    grades.insert(String::from("Joe"), 71); // overwite
    println!("{}", grades["Joe"]);

    grades.entry(String::from("Jane")).or_insert(80); // inserts if the key did not exist
    println!("{}", grades["Jane"]);

    grades.entry(String::from("Jane")).or_insert(81); // does not change the value
    println!("{}", grades["Jane"]);

    // inplace change of value (defaults to 0 if key does not exist)
    let value = grades.entry(String::from("Joe")).or_insert(0);
    *value += 1;
    println!("{}", grades["Joe"]);

    // the same, no need for temporary variable
    *grades.entry(String::from("Joe")).or_insert(0) += 1;
    println!("{}", grades["Joe"]);

    // This did not exists so defaults to 0
    *grades.entry(String::from("George")).or_insert(0) += 1;
    println!("{}", grades["George"]);
}
