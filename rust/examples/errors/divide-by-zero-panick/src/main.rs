fn div(a: i32, b: i32) -> i32 {
    a / b
}

fn main() {
    for number in [2, 4, 0, 20] {
        let res = div(100, number);
        dbg!(res);
    }
}
