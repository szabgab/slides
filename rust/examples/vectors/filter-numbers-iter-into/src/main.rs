fn main() {
    let numbers: Vec<i32> = vec![
      1, 2, 3, 4, 5, 6, 7, 8,
    ];

    let even_number = numbers
      .into_iter()
      .filter(|n| n % 2 == 0)
      .collect::<Vec<_>>();

    println!("{:?}", even_number);
}
