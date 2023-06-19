fn main() {
    let text = "mouse cat cat   oliphant";
    let parts = text.split_whitespace();
    // println!("{:?}", parts);
    for part in parts {
        println!("{}", part);
    }
}
