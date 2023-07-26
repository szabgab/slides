fn main() {
    let chars = vec!['a', 'b', 'c'];
    let mut c = 0;
    let pairs = chars.into_iter().rev().map(|letter| { c += 1; (letter, c) });
    for pair in pairs {
        println!("{pair:?}");
    }
}
