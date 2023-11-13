fn main() {
    let limit = 100;

    let result = count_in_process(limit);
    println!("{}", result);
    assert_eq!(result, limit);
}

fn count_in_process(limit: i32) -> i32 {
    let mut counter = 0;
    for _ in 0..limit {
        counter += 1;
    }

    counter
}

