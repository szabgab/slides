fn main() {
    let mut n = 1;
    println!("before: {n}");
    increment(&n);
    println!("after:  {n}");
}

fn increment(mut val: &i32) {
    println!("start:  {val}");
    val += 1;
    println!("end:    {val}");
}
