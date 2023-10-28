fn main() {
    let x = ();
    println!("{:?}", x);

    let y = ();
    println!("{:?}", y);

    let same = x == y;
    println!("{:?}", same);

    let res = empty();
    println!("{:?}", res);

    let res = no_return();
    println!("{:?}", res);
}

fn empty() {
}

fn no_return() {
    println!("Hello World!");
}
