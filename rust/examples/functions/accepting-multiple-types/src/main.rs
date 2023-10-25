//fn add(a: f32, b: f32) -> f32 {
//    a + b
//}
//fn add(a: i32, b: i32) -> i32 {
//    a + b
//}

fn add<T: Into<f64>>(a: T, b: T) -> f64 {
    a.into() + b.into()
}

fn main() {
    let sum = add(4.0, 7.0);
    println!("{sum}");

    let sum = add(5, 1);
    println!("{sum}");
}
