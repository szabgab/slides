fn main() {
    let mut limit = 10;
    loop {
        println!("count {}", limit);
        limit -= 1;
        if limit < 0 {
            break
        }
    }
}
