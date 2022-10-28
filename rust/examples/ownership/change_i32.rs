fn main() {
    let mut counter = 0;
    println!("Main: {counter}");
    display(counter);
    println!("Main: {counter}");
    increment(&mut counter);
    display(counter);
    println!("Main: {counter}");
}

fn display(cnt: i32) {
    println!("Display: {cnt}")
}


fn increment(cnt: &mut i32) {
    *cnt += 1;
}

