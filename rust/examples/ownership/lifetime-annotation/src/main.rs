fn main() {
    let a = "hello";
    let b = String::from("world");

    let c = longer(a, b.as_str());

    println!("c: {}", c);
}

fn longer<'a>(x: &'a str, y: &'a str) -> &'a str {
    if x.len() > y.len() {
        x
    } else {
        y
    }
}

