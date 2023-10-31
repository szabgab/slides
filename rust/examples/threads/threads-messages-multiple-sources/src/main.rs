use std::sync::mpsc;
use std::thread;
use std::time::Duration;


fn main() {
    let (tx1, rx) = mpsc::channel();
    let tx2 = tx1.clone();

    println!("{:?}: start", thread::current().id());

    thread::spawn(move || {
        for i in 1..=5 {
            thread::sleep(Duration::from_millis(1));
            tx1.send(format!("{:?}: {}", thread::current().id(), i)).unwrap();
        }
        println!("Spawned thread {:?} ends", thread::current().id());
    });

    thread::spawn(move || {
        for i in 1..=5 {
            thread::sleep(Duration::from_millis(1));
            tx2.send(format!("{:?}: {}", thread::current().id(), i)).unwrap();
        }
        println!("Spawned thread {:?} ends", thread::current().id());
    });

    for received in rx {
        println!("Got: {}", received);
    }

    println!("Main thread ends");
}

