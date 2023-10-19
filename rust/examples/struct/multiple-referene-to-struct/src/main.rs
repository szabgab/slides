#[derive(Debug)]
#[allow(dead_code)]
struct Something {
    number: i32,
    text: String,
    numbers: Vec<i32>,
}

fn main() {
    let a = Something {number: 2, text: "blue".to_string(), numbers: vec![5, 6]};
    dbg!(&a);

    let b = &a;
    dbg!(&b);
    dbg!(&a);
}

