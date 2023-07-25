fn main() {
    let string1 = String::from("Apple");
    let string2 = String::from("Banana");
    let str3    = "Peach";

    let other = [string1, string2, str3.to_string()].concat();
    println!("{other}");
}
