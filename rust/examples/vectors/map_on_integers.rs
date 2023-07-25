fn main() {
    let numbers = vec![1, 2, 3];
    println!("{:?}", numbers);
    let numbers: Vec<i32> = numbers.into_iter().map(|x| x + 1).collect();
    println!("{:?}", numbers);
}
