fn main() {
    let numbers: [i32; 3] = [10, 11, 12];

    for ix in 0..numbers.len() {
        println!("{ix} {}", numbers[ix]);
    }
}
