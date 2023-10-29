fn main() {
    let text = "Hello";
    println!("{}", text);
    let reversed = reverse(text);
    println!("{}", text);
    println!("{}", reversed);

}

fn reverse(text: &str) -> String {
    let reversed: String = text.chars().rev().collect();
    reversed
}
