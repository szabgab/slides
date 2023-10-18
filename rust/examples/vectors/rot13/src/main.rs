fn main() {
    let text = String::from("Hello World!");
    println!("{text}");
    let encrypted = rot13(text);
    println!("{encrypted}");
    let decrypted = rot13(encrypted);
    println!("{decrypted}");

    //let equal = text == decrypted;
    //println!("{equal}");
}

fn rot13(text: String) -> String {
    let mut chars:Vec<char> = vec![];
    let a = 'a' as u32;
    let z = 'z' as u32;
    let aa = 'A' as u32;
    let zz = 'Z' as u32;
    for ch in text.chars() {
        let mut code = ch as u32;
        // dbg!(code);
        if a <= code && code <= z {
            code = a + ((code - a + 13) % 26);
            let ch_new = char::from_u32(code).expect("Could not convert to char");
            chars.push(ch_new);
        } else if aa <= code && code <= zz {
            code = aa + ((code - aa + 13) % 26);
            let ch_new = char::from_u32(code).expect("Could not convert to char");
            chars.push(ch_new);
        } else {
            chars.push(ch);
        }
    }

    let other: String = chars.into_iter().collect();
    other
}
