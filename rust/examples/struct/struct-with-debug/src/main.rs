
#[derive(Debug)]
struct Red(i32);

fn main() {
    let red = Red(10);
    //println!("{}", red);  // `Red` doesn't implement `std::fmt::Display`
    println!("{:?}", red);  //  Red(10)
}
