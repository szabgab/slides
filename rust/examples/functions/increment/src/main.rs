fn main() {
    let mut n = 1;
    println!("before: {n}");
    increment(&mut n);
    println!("after:  {n}");
}

fn increment(val: &mut i32) {
    println!("start:  {val}");
    *val += 1;
    println!("end:    {val}");
}
