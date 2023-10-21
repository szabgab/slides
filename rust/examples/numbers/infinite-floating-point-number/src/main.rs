fn main() {
    let infinite = 1.0 / 0.0;
    println!("{}", infinite);

    let negative_infinite = 1.0 / -0.0;
    println!("{}", negative_infinite);

    let what = infinite + negative_infinite;
    println!("{}", what);

    // let infinite = 1/0;
    // ^^^ attempt to divide `1_i32` by zero
    //println!("{}", infinite);
}
