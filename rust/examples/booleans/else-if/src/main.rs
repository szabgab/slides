#[allow(clippy::comparison_chain)]
fn main() {
    let x = 23;
    let y = 32;
    if x > y {
        println!("x is bigger than y");
    } else if x < y {
        println!("x is smaller than y");
    } else {
        println!("x is equal to y");
    }
}
