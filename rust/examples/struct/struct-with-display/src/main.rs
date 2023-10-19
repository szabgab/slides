#[derive(Debug)]
struct Red(i32);

impl std::fmt::Display for Red {
    fn fmt(&self, format: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(format, "{}", self.0)
    }
}

fn main() {
    let red = Red(10);
    println!("{}", red);    // 10
    println!("{:?}", red);  //  Red(10)
}
