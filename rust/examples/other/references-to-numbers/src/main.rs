fn main() {
    let x = 2;
    let y = &2;
    println!("{}", x);
    println!("{}", y);

    println!("{}", &x == y);
    assert_eq!(&x, y);
}
