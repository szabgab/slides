fn main() {
    let x = "abc";
    let y = "abd";
    let z = "abd";
    println!("{}", x < y);
    println!("{:?}", x.cmp(y));
    println!("{}", y == z) ;
    println!("{:?}", y.cmp(y));
    println!();

    let x = "abc".to_string();
    let y = "abd".to_string();
    let z = "abd".to_string();
    println!("{}", x < y);
    println!("{:?}", x.cmp(&y));
    println!("{}", y == z) ;
    println!("{:?}", y.cmp(&y));
}

