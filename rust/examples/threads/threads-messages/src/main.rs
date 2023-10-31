use std::sync::mpsc;
use std::thread;
use std::time::Duration;


fn main() {
    let (tx, rx) = mpsc::channel();

    thread::spawn(move || {
        let val = String::from("Hello");
        tx.send(val).unwrap();

        for i in 1..=10 {
            thread::sleep(Duration::from_millis(1));
            tx.send(i.to_string()).unwrap();
        }
        println!("Spawned thread ends");
    });

    let received = rx.recv().unwrap();
    println!("Got: {}", received);

    // complex way for reveiving
    for _j in 1..=5 {
        let received = rx.recv().unwrap();
        println!("Got: {}", received);
    }
    println!();

    // simple code for receiving
    for received in rx {
        println!("Got: {}", received);
    }
    println!();

    println!("Main thread ends");
}

