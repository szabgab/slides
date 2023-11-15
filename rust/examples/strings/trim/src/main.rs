fn main() {
    let text = "  Some text  ".to_string();
    println!("original:   '{}'", text);
    println!("trim_end:   '{}'", text.trim_end());
    println!("trim_start: '{}'", text.trim_start());
    println!("trim:       '{}'", text.trim());
}
