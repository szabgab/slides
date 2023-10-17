fn main() {
    assert_eq!(commafy("56789012"), "56,789,012");
    assert_eq!(commafy("789012"), "789,012");
    assert_eq!(commafy("123"), "123");
    assert_eq!(commafy("1234"), "1,234");
}


fn commafy(text: &str) -> String {
    let mut chars: Vec<_> = text.chars().collect();
    let len = text.len();
    for i in (3..text.len()).step_by(3) {
        chars.insert(len-i, ',');
    }
    let commafied: String = chars.iter().collect();
    commafied
}

