pub fn commafy<Integer: Into<i64> +  Copy + std::fmt::Debug + std::fmt::Display>(num: Integer) -> String {
//pub fn commafy(num: i32) -> String {
    let num = format!("{num}");
    let mut ix = 0;
    let num = num.chars().rev().map(|chr| {
        ix += 1;
        if ix % 3 == 1 && ix > 1 { format!(",{chr}") } else { format!("{chr}") }
    }).collect::<String>();
    num.chars().rev().collect::<String>()
}

#[cfg(test)]
mod tests {
    use super::commafy;

    #[test]
    fn test_commafy() {
        assert_eq!("1", commafy(1));
        assert_eq!("12", commafy(12));
        assert_eq!("123", commafy(123));
        assert_eq!("1,234", commafy(1234));
        assert_eq!("12,345", commafy(12345));
        assert_eq!("123,456", commafy(123456));
        assert_eq!("1,234,567", commafy(1234567));

        assert_eq!("1,234", commafy(1234i16));
        assert_eq!("254", commafy(254u8));
        assert_eq!("1,254", commafy(1254u16));
    }
}

