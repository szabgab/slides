pub fn commafy(num: i32) -> String {
    let num = format!("{num}");
    num
}

#[cfg(test)]
mod tests {
    use super::commafy;

    #[test]
    fn test_commafy() {
        assert_eq!("1", commafy(1));
        assert_eq!("12", commafy(12));
        assert_eq!("123", commafy(123));
    }
}

