#[allow(dead_code)]
enum ColorName {
    Red,
    Green,
    Blue,
    White,
    Black,
}

fn main() {
    let background = ColorName::Black;
    let foreground = ColorName::White;
    let ink = ColorName::Black;
    let frame = ColorName::Red;

    for color in [background, foreground, ink, frame] {
        match color {
            ColorName::White => println!("white: #FFFFFF"),
            ColorName::Red => println!("red: #FF0000"),
            _ => println!("other"),
        }
    }
}
