fn main() {
    let text_1 = "Hello World!";
    println!("{text_1}");

    let text_2 = String::from("Hello World!");
    println!("{text_2}");

    let text_3 = "Hello World!".to_string();
    println!("{text_3}");

    let text_4 = "Hello World!".to_owned();
    println!("{text_4}");

    assert_eq!(text_1, "Hello World!");
    assert_eq!(text_1, text_2);
}
