fn main() {
    let n = 1;
    println!("before: {n}");

    do_something(n);
    println!("after:  {n}");
}

fn do_something(mut val: i32) {
    println!("start:  {val}");
    val += 1;
    println!("end:    {val}");
}
