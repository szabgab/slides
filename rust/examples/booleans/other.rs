fn main() {
    let x = 3;
    if x {      // expected `bool`, found integer
        println!("x is true");
    }
}
