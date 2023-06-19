fn main() {
    let mut numbers: [i32; 3] = [10, 11, 12];

    println!("{:?}", numbers);

    numbers[0] = 30;
    println!("{:?}", numbers);
}
