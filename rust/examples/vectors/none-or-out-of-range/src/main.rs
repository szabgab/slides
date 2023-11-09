fn main() {
    let numbers_real: Vec<Option<i32>> = vec![Some(3),  None];
    println!("{:?}", numbers_real);

    println!("{:?}", numbers_real[1]);      // None
    println!("{:?}", numbers_real.get(1));  // Some(None)
    // println!("{:?}", numbers_real[17]); // panic: index out of bounds: the len is 2 but the index is 17
    println!("{:?}", numbers_real.get(17)); // None    - out of range!
    println!();

    println!("{:?}", numbers_real.get(1).is_none());
    println!("{:?}", numbers_real.get(17).is_none()); // out of range!
    println!();

    println!("{:?}", numbers_real.get(1).is_some());
    println!("{:?}", numbers_real.get(17).is_some()); // out of range!
    println!();

}
