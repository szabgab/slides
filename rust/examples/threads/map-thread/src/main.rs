use std::sync::mpsc;
use std::thread;

fn main() {
    let numbers: Vec<i32> = (1..=10).collect();
    println!("{:?}", numbers);

    let doubles = numbers.iter().map(|num| 2 * num).collect::<Vec<i32>>();
    println!("{:?}", doubles);

    let doubles = numbers.iter().map(double_function).collect::<Vec<i32>>();
    println!("{:?}", doubles);

    let doubles = map_thread(&numbers, double_function, 3);
    println!("{:?}", doubles);
}

fn double_function(num: &i32) -> i32 {
    2 * num
}

fn map_thread(numbers: &[i32], func: fn(&i32) -> i32, max_threads: i32) -> Vec<i32> {
    //numbers.iter().map(double_function).collect::<Vec<i32>>()
    //numbers.iter().map(func).collect::<Vec<i32>>()

    let (tx, rx) = mpsc::channel();
    let mut thread_count = 0;
    let mut started = 0;
    let mut finished = 0;
    let mut results: Vec<(i32, i32)> = vec![];

    for numberx in numbers.iter() {
        let number = *numberx;
        started += 1;
        let mytx = tx.clone();
        thread::Builder::new().name(format!("{}", started)).spawn(move || {
            let id: i32 = thread::current().name().unwrap().parse().unwrap();
            let res = func(&number);
            mytx.send((id, res)).unwrap();
        }).unwrap();

        thread_count += 1;
        if thread_count >= max_threads {
            let received = rx.recv().unwrap();
            results.push(received);
            finished += 1;
        }
    }

    for received in rx {
        //println!("received {}", thread_count);
        finished += 1;
        results.push(received);
        if finished >= started {
            break;
        }
    }

    results.sort();
    results.iter().map(|item| item.1).collect::<Vec<i32>>()

}
