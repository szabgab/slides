fn main() {
    let text = "Hello World!";
    println!("{text}");
    let encrypted = rot13(text);
    println!("{encrypted}");
    //let decrypted = rot13(encrypted);
    //println!("{decrypted}");

    //let equal = text == decrypted;
    //println!("{equal}");
}

fn rot13(text: &str) -> &str {
    let mut chars:Vec<char> = vec![];
    let mut strs:Vec<String> = vec![];
    let a = 'a' as u32;
    let z = 'z' as u32;
    for ch in text.chars() {
        // dbg!(ch);
        let mut code = ch as u32;
        dbg!(code);
        if a <= code && code <= z {
            code = a + ((code - a + 13) % 26);
            //dbg!(code);
            //
            let ch_new = char::from_u32(code).expect("Could not convert to char");
            chars.push(ch_new);
            strs.push(ch_new.to_string());
            //code = code + 13
        }
    }
    //chars.iter().collect()
    strs.iter().collect()
    //text
}
