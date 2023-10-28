//fn increment(mut x: i32) -> i32 {
//    x += 1;
//    x
//}

fn increment(x: i32) -> i32 {
    x + 1
}

fn main() {
    let mut a = 1;
    println!("{a}");
    a = increment(a);
    println!("{a}");
}
