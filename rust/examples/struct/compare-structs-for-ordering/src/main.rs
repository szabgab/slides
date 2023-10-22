#[derive(PartialEq, Eq, PartialOrd, Ord)]
struct Thing {
    number: i32,
    name: String,
}


fn main() {
    let a = Thing {
        number: 42,
        name: "Foo".to_string(),
    };

    let b = Thing {
        number: 43,
        name: "Foo".to_string(),
    };

    let c = Thing {
        number: 42,
        name: "Bar".to_string(),
    };

    let d = Thing {
        number: 43,
        name: "Bar".to_string(),
    };

    println!("{}", a < b); // becasue 42 < 43
    println!("{}", c < b); // becasue 42 < 43 ( Bar < Foo is not even checked here)
    println!("{}", c < a); // because Bar < Foo
    println!("{}", c < d); // because 42 < 43
    println!("{}", a < d); // because 42 < 43
                           // the comparisions is in the order of declaraion of the fields
                           // So the `name` field is not checked here

}
