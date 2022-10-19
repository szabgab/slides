fn main() {
    let x = 3;
    let y = 4;
    if x < y {
        println!("{} is bigger than {}", y, x);
    }

    let z = x < y;
    println!("{}", z);
    let z =  x > y;
    println!("{}", z);

    let t = true;
    if t {
        println!("t is true");
    }

    // if x {
    //     println!("x is true");
    // }
    // expected `bool`, found integer

}
