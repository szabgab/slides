fn main() {
    let numbers: [i32; 3] = [10, 11, 12];

    println!("{:?}", numbers);

    numbers[0] = 30; // cannot assign to `numbers[_]`, as `numbers` is not declared as mutable
    println!("{:?}", numbers);
}
