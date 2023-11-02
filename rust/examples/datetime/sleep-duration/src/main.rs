fn main() {
    let start = std::time::Instant::now();
    println!("{:?}", start);
    std::thread::sleep(std::time::Duration::from_secs(1));
    let end = std::time::Instant::now();
    println!("{:?}", end);
    let elapsed = end - start;
    println!("{:?}", elapsed);
    println!("{:?}", start.elapsed());

}
