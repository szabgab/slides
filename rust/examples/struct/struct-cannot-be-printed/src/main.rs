struct Red(i32);

fn main() {
    #[allow(unused_variables)]
    let red = Red(10);
    // println!("{}", red);  // `Red` doesn't implement `std::fmt::Display`
    // println!("{:?}", red);  //  `Red` doesn't implement `Debug`
}
