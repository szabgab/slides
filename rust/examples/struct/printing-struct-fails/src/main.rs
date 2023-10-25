#[allow(dead_code)]
struct Animal<'a> {
    name: &'a str,
    size: &'a str,
    weight: i32,
}

fn main() {
    #[allow(unused_variables)]
    let a = Animal {name: "elephant", size: "huge", weight: 100};
    //println!("{}", a);   // `Animal<'_>` doesn't implement `std::fmt::Display`
    // println!("{:?}", a); // `Animal<'_>` doesn't implement `Debug`
    // dbg!(a);             // `Animal<'_>` doesn't implement `Debug`
}

