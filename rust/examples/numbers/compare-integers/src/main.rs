fn main() {
    let x = 1;
    let y = 2;
    let z = 1;
    println!("{}", x < y);
    println!("{:?}", x.cmp(&y));
    println!("{}", y < x);
    println!("{:?}", y.cmp(&x));
    println!("{}", x < z);
    println!("{:?}", x.cmp(&z));
    println!();


    let x: u8 = 1;
    let y: u8 = 2;
    println!("{}", x < y);
    println!("{:?}", x.cmp(&y));
}
