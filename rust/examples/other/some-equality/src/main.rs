#[allow(clippy::unnecessary_literal_unwrap)]
fn main() {
    let x = Some(3);
    let y = Some(3);
    println!("{:?}", x); // `Option<{integer}>` cannot be formatted with the default formatter
    println!("{}", x == y);

    let z = Some(&3);
    println!("{:?}", z); // `Option<&{integer}>` cannot be formatted with the default formatter
    println!("{}", &x.unwrap() == z.unwrap());
}
