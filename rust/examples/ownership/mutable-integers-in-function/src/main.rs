fn increment(x: &mut i32) {
    *x += 1;
}

fn main() {
    let mut a = 1;
    println!("{a}");
    increment(&mut a);
    println!("{a}");
}

