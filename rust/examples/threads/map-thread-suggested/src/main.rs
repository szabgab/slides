use std::sync::{Condvar, Mutex};
use std::thread;

fn main() {
    let numbers: Vec<i32> = (1..=10).collect();
    println!("{:?}", numbers);

    let doubles = map_thread(&numbers, double_function, 3);
    println!("{:?}", doubles);
}

fn double_function(num: &i32) -> i32 {
    //println!("{:?}", std::thread::current().id());
    2 * num
}

fn map_thread<Tin: Sync, Tout: Send>(
    params: &[Tin],
    func: fn(&Tin) -> Tout,
    max_threads: i32,
) -> Vec<Tout> {
    let thread_count = Mutex::new(0);
    let notify_finish = Condvar::new();

    // Use scoped threads so that we can pass references around
    thread::scope(|scope| {
        let mut handles = vec![];
        for xref in params {
            // Wait for earlier threads to finish, if necessary
            let mut guard = thread_count.lock().unwrap();
            while *guard >= max_threads {
                guard = notify_finish.wait(guard).unwrap();
            }

            // Increment running thread count
            *guard += 1;

            handles.push(scope.spawn(|| {
                // Run calculation
                let res = func(xref);

                // Report success, decrement running thread count
                *(thread_count.lock().unwrap()) -= 1;
                notify_finish.notify_one();

                // Return calculation result
                res
            }));
        }

        // Read the return values of each thread, in order
        handles.into_iter().map(|h| h.join().unwrap()).collect()
    })
}
