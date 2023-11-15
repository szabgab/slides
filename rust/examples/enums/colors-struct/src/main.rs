#[allow(dead_code)]
enum ColorName {
    Red,
    Green,
    Blue,
    White,
    Black,
}

struct Color {
    name: ColorName,
    rgb: String,
}


fn main() {
    let background = Color {
        name: ColorName::Black,
        rgb : "#000000".to_string(),
    };
    let foreground = Color {
        name: ColorName::White,
        rgb: "#FFFFFF".to_string(),
    };
    let ink = Color {
        name: ColorName::Black,
        rgb: "#FFFFFF".to_string(),
    };
    let frame = Color {
        name: ColorName::Red,
        rgb: "#FF0000".to_string(),
    };

    for color in [background, foreground, ink, frame] {
        match color.name {
            ColorName::White => println!("white: {}", color.rgb),
            ColorName::Red => println!("red: {}", color.rgb),
            _ => println!("other"),
        }
    }
}
