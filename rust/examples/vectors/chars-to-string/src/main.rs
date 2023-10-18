fn main() {
    let text = "The black cat";
    let reversed: String = text.chars().rev().collect();
    println!("{text}");
    println!("{reversed}");

    println!("{:?}", text.chars());
    let res: String = text.chars().collect();
    println!("{res}");

    let letters:Vec<char> = vec!['R', 'u', 's', 't'];
    let name: String = letters.into_iter().collect();
    println!("{name}");
}
