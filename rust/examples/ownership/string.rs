fn main() {
    let x = String::from("Foo Bar");
    println!("{x}");
    let y = x;
    println!("{y}");
    //println!("{x}"); // borrow of moved value: `x`
}
