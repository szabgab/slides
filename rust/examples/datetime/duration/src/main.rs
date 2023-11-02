fn main() {
    let duration = std::time::Duration::from_secs(3);
    println!("as is       {:?}", duration);
    println!("as seconds: {:?}", duration.as_secs());
    println!("as millis:  {:?}", duration.as_millis());
    println!("as micros:  {:?}", duration.as_micros());
    println!("as nanos:   {:?}", duration.as_nanos());
    println!();

    let dur = std::time::Duration::new(2, 4);
    println!("{:?}", dur);
    println!("as seconds: {:?}", dur.as_secs());
    println!();

    let d = duration + dur;
    println!("{:?}", d);

    let d = duration - dur;
    println!("{:?}", d);
}
