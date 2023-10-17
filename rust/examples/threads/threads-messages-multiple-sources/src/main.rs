use std::sync::mpsc;
use std::thread;
use std::time::Duration;


fn main() {
    let (tx1, rx) = mpsc::channel();
    let tx2 = tx1.clone();


    thread::spawn(move || {
        for i in 1..=5 {
            thread::sleep(Duration::from_millis(1));
            tx1.send(format!("1: {i}")).unwrap();
        }
        println!("Spawned thread 1 ends");
    });

    thread::spawn(move || {
        for i in 1..=5 {
            thread::sleep(Duration::from_millis(1));
            tx2.send(format!("2: {i}")).unwrap();
        }
        println!("Spawned thread 2 ends");
    });

    for received in rx {
        println!("Got: {}", received);
    }

    println!("Main thread ends");
}

