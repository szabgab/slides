#[allow(clippy::iter_skip_next)]
fn main() {
    let text = "The black cat";

    println!("{}", text);
    println!("{:?}", text.chars());
    println!("{:?}", text.chars().nth(4));
    //println!("{:?}", text.chars().skip(4).nth(0));
    println!("{:?}", text.chars().skip(4).next());
    println!("{:?}", text.chars().nth(20));

    println!("--------");

    for n in [-1, 4, 20] {
        let char = text.chars().nth(n as usize);
        println!("{:?}", char);
        match char {
            Some(value) => println!("{}", value),
            None => println!("This was None"),
        }
    }
}
