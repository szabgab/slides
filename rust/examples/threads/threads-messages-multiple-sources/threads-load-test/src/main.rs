use std::time::Instant;
use std::sync::mpsc;
use std::thread;

fn main() {
    let (tx, rx) = mpsc::channel();

    let start = Instant::now();
    //for n in 1..=10 {
    //    println!("{n}: {}", fibonacci(n));
    //}

    //let n = 43; // 42 2 sec,   43 3 sec
    //println!("{n}: {}", fibonacci(n));

    //for _x in 1..=10 {
    //    let n = 42;
    //    println!("{n}: {}", fibonacci(n));
    //}

    for _x in 1..=10 {
        let txr = tx.clone();
        let n = 42;
        thread::spawn(move || {
            let res = fibonacci(n);
            txr.send(res.to_string()).unwrap();
            println!("spawned thread finished");
        });
    }
    drop(tx);

    for received in rx {
        println!("Got: {}", received);
    }

    let duration = start.elapsed();

    println!("Time elapsed in expensive_function() is: {:?}", duration);

}

fn fibonacci(n :u64) -> u64 {
    if n == 0 || n == 1 {
        return 1;
    }
    fibonacci(n - 1) + fibonacci(n - 2)
}
