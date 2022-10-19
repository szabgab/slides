fn main() {
    let x = 300000000;
    // let x = 3000000000;
    // note: the literal `3000000000` does not fit into the type `i32` whose range is `-2147483648..=2147483647`
    let y: i64 = 3000000000;
    println!("{}", x);
    println!("{}", y);

    println!("{}", x+y);
}

