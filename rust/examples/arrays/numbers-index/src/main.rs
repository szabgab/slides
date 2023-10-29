fn main() {
    let numbers: [i32; 3] = [10, 11, 12];

    for (ix, number) in numbers.iter().enumerate() {
        println!("{ix} {}", number);
    }
}
