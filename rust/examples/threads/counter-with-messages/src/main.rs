fn main() {
    let limit = 100;

    let result = count_with_messages(limit);
    println!("{}", result);
    assert_eq!(result, limit);
}

fn count_with_messages(limit: i32) -> i32 {
    let mut counter = 0;
    let (tx1, rx) = std::sync::mpsc::channel();
    for _ in 0..limit {
        let tx2 = tx1.clone();

        std::thread::spawn(move || {
            //println!("{:?}", std::thread::current().id());
            tx2.send(1).unwrap();
        });
    }

    drop(tx1); // we need to close this Sender so the next loop will end properly

    for received in rx {
        counter += received;
    }

    counter
}
