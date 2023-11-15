#[derive(PartialEq)]
#[allow(dead_code)]
enum ColorName {
    Red,
    Green,
    Blue,
    White,
    Black,
}

// We need the allow dead_code beacause in this exampl we did not use all the values that were listed in the enum

fn main() {
    let background = ColorName::Black;
    let foreground = ColorName::White;
    let ink = ColorName::Black;

    // This comparision requires the PartialEq trait
    println!("{}", background == foreground);
    println!("{}", background == ink);
}
