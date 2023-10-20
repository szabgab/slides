#[derive(PartialEq, PartialOrd)]
struct Thing {
    number: i32,
    float: f32,
}


fn main() {
    let a = Thing {
        number: 42,
        float: 1.0,
    };

    let b = Thing {
        number: 43,
        float: 1.0,
    };

    let c = Thing {
        number: 42,
        float: 0.9,
    };

    let d = Thing {
        number: 43,
        float: 0.9,
    };


    println!("{}", a < b); // becasue 42 < 43
    println!("{}", c < b); // becasue 42 < 43 and also 0.9 < 1.0
    println!("{}", c < a); // because 0.0 < 1.0
    println!("{}", c < d); // because 42 < 43
    println!("{}", a < d); // because 42 < 43
                           // the comparisions is in the order of declaraion of the fields

}
