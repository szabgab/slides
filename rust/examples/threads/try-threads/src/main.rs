use std::thread;
use std::time::Duration;

fn main() {
    println!("Before starting: {:?}", thread::current().id());

    let handle = thread::spawn(|| {
        for i in 1..10 {
            println!("hi number {} from the spawned thread! {:?}", i, thread::current().id());
            thread::sleep(Duration::from_millis(1));
        }
        println!("spwaned thread ended");
    });

    for i in 1..5 {
        println!("hi number {} from the main thread! {:?}", i, thread::current().id());
        thread::sleep(Duration::from_millis(1));
    }

    println!("main thread ended");
    handle.join().unwrap(); // waiting for the other thread to end.
    println!("After ending: {:?}", thread::current().id());

    println!("exiting");
}
