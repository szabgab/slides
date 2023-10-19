#[derive(Debug)]
struct Color(u8, u8, u8);

impl std::fmt::Display for Color {
    fn fmt(&self, format: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(format, "RGB({}, {}, {})", self.0, self.1, self.2)
    }
}

fn main() {
    let black = Color(0, 0, 0);
    println!("{}", black);    // RGB(0, 0, 0)
    println!("{:?}", black);  // Color(0, 0, 0)

    let white = Color(255, 255, 255);
    println!("{}", white);    // RGB(255, 255, 255)
    println!("{:?}", white);  // Color(255, 255, 255)

    let red = Color(255, 0, 0);
    println!("{}", red);    // RGB(255, 0, 0)
    println!("{:?}", red);  // Color(255, 0, 0)
}
