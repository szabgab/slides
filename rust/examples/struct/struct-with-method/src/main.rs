#[derive(Debug)]
struct Color {
    red: u8,
    green: u8,
    blue: u8
}

impl std::fmt::Display for Color {
    fn fmt(&self, format: &mut std::fmt::Formatter) -> std::fmt::Result {
        write!(format, "RGB({}, {}, {})", self.red, self.green, self.blue)
    }
}

impl Color {
    fn hex(&self) -> String {
        format!("#{:X}{:X}{:X}", self.red, self.green, self.blue)
    }
}


fn main() {
    let color = Color { red: 80, green: 123, blue: 241 };
    println!("{}", color);
    println!("{:?}", color);
    println!("{}", color.hex());
}
