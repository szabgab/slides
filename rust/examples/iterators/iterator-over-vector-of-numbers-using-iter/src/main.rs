fn main() {
    let numbers = vec![1, 2, 3];

    println!("{:?}", &numbers);
    for n in numbers.iter() {
        println!("{}", n);
    }
    println!("{:?}", numbers);
}
