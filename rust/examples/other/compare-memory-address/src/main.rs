fn main() {
    let text_a = "Hello, world!".to_string();
    let text_b = "Hello, world!".to_string();
    println!("{}", text_a == text_b);
    println!("{}", std::ptr::addr_of!(text_a) == std::ptr::addr_of!(text_b));
    println!("{:?}", &std::ptr::addr_of!(text_a));
    println!("{:?}", &std::ptr::addr_of!(text_b));
}
