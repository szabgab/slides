fn main() {
    let numbers_real: Vec<Option<i32>> = vec![Some(3), None, Some(7)];
    println!("{:?}", numbers_real);

    let numbers_ref: Vec<Option<&i32>> = vec![Some(&3), None, Some(&7)];
    println!("{:?}", numbers_ref);

    println!("{:?}", numbers_real[1]);
    println!("{:?}", numbers_real.get(1));
    println!("{:?}", numbers_real.get(7));

    //for i in 0..numbers_real.len() {
    //    println!("{:?}", numbers_real[i] == numbers_ref[i]);
    //}
    //
}
