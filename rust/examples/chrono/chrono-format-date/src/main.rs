use chrono::{DateTime, Utc};

fn main() {
    let now: DateTime<Utc> = Utc::now();
    println!("{}", now);
    println!("{}", now.format("%Y-%m-%d %H:%M:%S.%f %Z"));
}
