fn main() {
    let numbers = vec![1, 2, 3];

    println!("{:?}", &numbers);

    for n in &numbers {
        println!("{}", n);
    }
    println!("{:?}", numbers);
}


