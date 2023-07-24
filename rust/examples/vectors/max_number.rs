fn main() {
    let numbers = vec![10, 29, 3, 47, 8, 19];
    println!("{:?}", &numbers);
    let max = numbers.iter().max();
    println!("{:?}", max);

    match max {
        Some(&max_value) => println!("Maximum is {}", max_value),
        None => println!("The vector was empty!"),
    }

    let numbers :Vec<i32> = vec![];
    println!("{:?}", &numbers);
    let max = numbers.iter().max();
    println!("{:?}", max);

    match max {
        Some(&max_value) => println!("Maximum is {}", max_value),
        None => println!("The vector was empty!"),
    }

}
