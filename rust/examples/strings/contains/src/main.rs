fn main() {
    let text = "The black cat climed the green tree";
    println!("{}", text.contains("cat"));
    println!("{}", text.contains("dog"));
    println!("{}", text.find("cat").unwrap());

    // println!("{}", text.find("dog").unwrap()); // panics

    println!("{}", text.find('a').unwrap());
    println!("{}", text[7..].find('a').unwrap());
}
