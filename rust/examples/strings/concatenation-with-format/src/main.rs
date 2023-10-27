fn main() {
    let string1 = String::from("Apple");
    let string2 = String::from("Banana");
    let str3    = "Peach";

    let text = format!("{}-{}-{}-{}", string1, string2, str3, "other");
    println!("{}", text);
    println!("{}", string1);
    println!("{}", string2);
    println!("{}", str3);
}

