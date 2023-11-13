fn main() {
    let limit = 100;

    let result = count_with_mutex(limit);
    println!("{}", result);
    assert_eq!(result, limit);
}

fn count_with_mutex(limit: i32) -> i32 {
    let counter = std::sync::Mutex::new(0);

    std::thread::scope(|scope| {
        for _ in 0..limit {
            scope.spawn(|| {
                let mut guard = counter.lock().unwrap();
                *guard += 1;
            });
        }
    });

    counter.into_inner().unwrap()
}

