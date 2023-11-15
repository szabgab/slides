#[allow(dead_code)]
enum ColorName {
    Red(String),
    Green(String),
    Blue(String),
    White(String),
    Black(String),
}


fn main() {
    let background = ColorName::Black("#000000".to_string());
    let foreground = ColorName::White("#FFFFFF".to_string());
    let ink = ColorName::Black("#FFFFFF".to_string());
    let frame = ColorName::Red("#FF0000".to_string());

    for color in [background, foreground, ink, frame] {
        match color {
            ColorName::White(val) => println!("white: {val}"),
            ColorName::Red(_val) => println!("red:"),
            _ => println!("other"),
        }
    }
}
