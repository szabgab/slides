fn main() {
    let mut numbers = vec![10, 11, 12];
    numbers.push(23);

    println!("{}", numbers.len());

    for num in numbers {
        println!("{}", num);
    }

}
