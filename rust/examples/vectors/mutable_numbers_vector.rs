fn main() {
    let mut numbers = vec![10, 11, 12];
    println!("{}", numbers.len());
    println!("{:?}", numbers);

    numbers.push(23);

    println!("{}", numbers.len());
    println!("{:?}", numbers);
}
