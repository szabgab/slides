use chrono::{DateTime, Utc, Local};

fn main() {
    let utc: DateTime<Utc> = Utc::now();
    println!("utc:           {}", utc);
    println!("utc timestamp: {}", utc.timestamp());
    println!("utc format:    {}", utc.format("%Y-%m-%d"));

    println!();
    let local: DateTime<Local> = Local::now();
    println!("{}", local);
    println!("{}", local.timestamp());


    let text = "2023-08-30T12:30:01+0000".to_string();
    let dt = DateTime::parse_from_str(&text, "%Y-%m-%dT%H:%M:%S%z").unwrap();
    println!();
    println!("dt:           {}", dt);
    println!("dt format:    {}", dt.format("%Y-%m-%d"));
    println!("dt format:    {}", dt.format("%H::%M::%S"));
}
