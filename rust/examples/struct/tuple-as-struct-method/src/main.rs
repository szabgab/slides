#[derive(Debug)]
struct Color(u8, u8, u8);

impl std::fmt::Display for Color {
    fn fmt(&self, format: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(format, "RGB({}, {}, {})", self.0, self.1, self.2)
    }
}

impl Color {
    fn hex(&self) -> String {
        format!("#{:X}{:X}{:X}", self.0, self.1, self.2)
    }
}

fn main() {
    let color = Color(80, 123, 241);
    println!("{}", color);
    println!("{:?}", color);

    println!("{}", color.hex());
}
