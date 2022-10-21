fn main() {
    let text = "The black cat climbed the green tree!";
    println!("{}", text);
    println!("{:?}", text.chars());
    println!("{:?}", text.chars().nth(4));
    println!("{:?}", text.chars().skip(4).nth(0));
}
