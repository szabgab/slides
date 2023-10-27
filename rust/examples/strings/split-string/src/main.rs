fn main() {
    let text = "mouse cat cat   oliphant";
    println!("{text}");
    let parts = text.split(' ');
    // println!("{:?}", parts);
    for part in parts {
        println!("{}", part);
    }
}
