fn main() {
    let x = 2;
    println!("{x}");

    let y = {
        let a = 2;
        let b = 3;
        a + b   // no semi-colon here!
    };          // there is a semi-colon here!
    println!("{y}");
}
