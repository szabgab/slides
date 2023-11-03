fn main() {
    let start = std::time::Instant::now();
    for number in 2..=100000 {
        let _prime = is_prime(number);
        //println!("{} {}", number, prime);
    }
    let end = std::time::Instant::now();

    println!("{:?}", start);
    println!("{:?}", end);
    let elapsed = end - start;
    println!("{:?}", elapsed);
    println!("{:?}", start.elapsed());
    println!("milliseconds: {:?}", start.elapsed().as_millis());
    println!("seconds:      {:?}", start.elapsed().as_secs());
}

fn is_prime(number: u32) -> bool {
    for div in 2..number {
        if number % div == 0 {
            return false;
        }
    }
    true
}


