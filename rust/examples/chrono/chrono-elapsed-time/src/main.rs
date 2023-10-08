use chrono::{DateTime, Utc};
use std::{thread, time};

fn main() {
    let start: DateTime<Utc> = Utc::now();
    println!("start:             {}", start);
    println!("start timestamp:   {}", start.timestamp());
    println!("start timestamp:   {}", start.timestamp_micros());
    println!();

    let ten_millis = time::Duration::from_millis(10);
    let now = time::Instant::now();

    thread::sleep(ten_millis);
    println!("elapsed as_micros: {}", now.elapsed().as_micros());
    println!("elapsed as_millis: {}", now.elapsed().as_millis());

    let end: DateTime<Utc> = Utc::now();
    println!();
    println!("end:               {}", end);
    println!("end timestamp:     {}", end.timestamp());
    println!("end timestamp:     {}", end.timestamp_micros());

    println!();
    println!("Elapsed (sec):     {}", end.timestamp()-start.timestamp());
    println!("Elapsed (millis):  {}", end.timestamp_millis()-start.timestamp_millis());
    println!("Elapsed (micros):  {}", end.timestamp_micros()-start.timestamp_micros());

}
