#[derive(PartialEq)]
struct Thing {
    name: String,
    number: i32,
    float: f32,
}

fn main() {
    let a = Thing {
        name: "Foo".to_string(),
        number: 42,
        float: 1.0,
    };

    let b = Thing {
        name: "Foo".to_string(),
        number: 42,
        float: 1.0,
    };

    let c = Thing {
        name: "Foo1".to_string(),
        number: 42,
        float: 1.0,
    };

    println!("{}", a == b);
    println!("{}", a == c);

    // must implement `PartialOrd`
    // println!("{}", a < c);
}
