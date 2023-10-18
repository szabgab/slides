// However this is also the same
fn main() {
    let chars = vec!['a', 'b', 'c'];
    let mut c = 0;
    let pairs = chars.into_iter().map(|letter| { c += 1; (letter, c) }).rev();
    for pair in pairs {
        println!("{pair:?}");
    }
}
