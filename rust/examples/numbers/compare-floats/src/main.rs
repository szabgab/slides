fn main() {
    let x = 1.0;
    let y = 2.0;
    let z = 1.0;
    println!("{}", x < y);
    //println!("{:?}", x.cmp(&y)); // can't call method `cmp` on ambiguous numeric type `{float}`
                                 // If we write x :f32 as Rustc suggests we get:
                                 // ^^^ `f32` is not an iterator
    println!("{}", x == z);
    println!();


    let x = 0.1 + 0.2;
    let y = 0.3;
    println!("{}", x);
    println!("{}", y);
    println!("{}", x == y);
}
