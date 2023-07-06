fn main() {
    let a = "hello";
    let b = "hello";
    let c = String::from("hello");
    let d = String::from("hello");

    println!("{}", a == b);
    println!("{}", a == c);
    println!("{}", c == d);
}


