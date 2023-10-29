fn main() {
    let fname = "Foo";
    let lname = "Bar";
    println!("{} {}", fname, lname);
    {
        let fname = "Peti";
        println!("{} {}", fname, lname);
    }
    println!("{} {}", fname, lname);
}
