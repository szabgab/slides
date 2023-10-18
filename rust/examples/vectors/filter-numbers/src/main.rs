fn main() {
    let numbers: Vec<i32> = vec![-7, 0, 1, 2, 22, 23];
    dbg!(&numbers);

    let same_numbers: Vec<i32> = numbers.iter().filter(|_number| true).cloned().collect();
    dbg!(&same_numbers);

    let positive_numbers: Vec<i32> = numbers.iter().filter(|number| number.is_positive()).cloned().collect();
    dbg!(&positive_numbers);

    let big_numbers: Vec<i32> = numbers.iter().filter(|number| number > &&12).cloned().collect();
    dbg!(&big_numbers);
}
